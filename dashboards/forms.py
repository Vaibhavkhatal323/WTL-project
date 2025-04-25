from django import forms
from blogs.models import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','category','author','blog_image','short_description','blog_body','is_featured','status',) 

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'      


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')       

