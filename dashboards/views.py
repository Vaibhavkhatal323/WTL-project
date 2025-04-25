from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib import messages
from blogs.models import Blogs 
from django.contrib.auth.models import User
from .forms import AddUserForm,EditPostForm,EditUserForm



@login_required(login_url='login')
def dashboard(request):
    category_counts=Category.objects.all().count()
    blogs_counts=Blogs.objects.all().count()
    context={
        'category_counts':category_counts,
        'blogs_count':blogs_counts
    }
    return render(request, 'dashboard/dashboard.html',context)  # Ensure 'dashboard.html' exists in templates

def categories(request):

    return render(request, 'dashboard/categories.html')

def add_categories(request):
    if request.method=="POST":
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context = {
        'form':form
    }

    return render(request, 'dashboard/add_categories.html', context)    

def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method=="POST":
        form =CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }

    return render(request, 'dashboard/edit_categories.html',context)  


def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')   


def posts(request):
    posts = Blogs.objects.all()
    context ={
        'posts':posts
    }
    return render(request, 'dashboard/posts.html',context)     



def add_posts(request):
    if request.method=="POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            print("Success")
            return redirect('posts')
        else:
            print("form.errors")        
    form = BlogPostForm()
    context ={
        'form':form

    }
    return render(request, 'dashboard/add_posts.html',context)   

def edit_post(request, pk):
    post = get_object_or_404(Blogs, pk=pk)  # Retrieve the post using its primary key
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)  # Bind the form to the post instance
        if form.is_valid():
            post = form.save(commit=False)  # Save the form without committing to the database yet
            title = form.cleaned_data.get('title')  # Retrieve the updated title
            post.slug = slugify(title)  # Update the slug based on the new title
            post.save()  # Save the updated post instance
            return redirect('posts')  # Redirect to the posts list after saving
    else:
        form = EditPostForm(instance=post)  # Prepopulate the form with the current post data

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)




    
def delete_post(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'dashboard/users.html',context)


def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to the users listing page
        else:
            print(form.errors)  # Print form errors to help debug
    else:
        form = AddUserForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_users.html', context)


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method =="POST":
        
        form = EditUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('users')

    form = EditUserForm(instance = user)
    context = {
        'form':form,
        'user':user

    }
    return render(request, 'dashboard/edit_user.html',context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')    