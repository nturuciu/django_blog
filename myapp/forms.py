from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post

        fields= ['title', 'slug', 'post_image', 'author']

class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        