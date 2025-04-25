from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from .models import Blogs, Category, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect


def posts_by_category(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blogs.objects.filter(category=category)
    if not posts.exists():
        return HttpResponse(f"No posts found in category {category.category_name}")
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
    
#blogs

def blogs(request, slug):

    # Handle POST request to save the comment
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    if request.method == "POST":
        if request.user.is_authenticated:
            comment_text = request.POST.get('comment')
            if comment_text:
                comment = Comment()
                comment.user = request.user
                comment.blog = single_post # Use the correct variable 'blog' here
                comment.comment = request.POST['comment']
                comment.save()

            # Redirect to the same page to display the new comment
                return HttpResponseRedirect(request.path_info)
        else:
            # If the user is not authenticated, redirect to login page
            return redirect('login')

    # Fetch all comments related to the current blog post
    comments = Comment.objects.filter(blog=single_post)  # Use the correct variable 'blog' here

    comment_count = comments.count()

    # Add comments and other data to the context
    context = {
        'single_post': single_post,  # Make sure the correct variable 'blog' is passed to the template
        'comments': comments,
        'comment_count': comment_count
    }

    return render(request, 'blogs.html', context)
    


   #search Functionality
def search(request):
    keyword=request.GET.get('keyword')

    blogs = Blogs.objects.filter(
    Q(title__icontains=keyword) |
    Q(short_description__icontains=keyword) |
    Q(blog_body__icontains=keyword),
    status='published'
)
    content={
        'blogs':blogs,
        'keyword':keyword
    }
  
    return render(request,'search.html',content)

