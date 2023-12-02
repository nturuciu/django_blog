# from django.contrib import admin
# from .models import Category
# from .models import Post
from .models import Blog
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

# # Register your models here.


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name')}

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('title')}  
#     list_display = ('title', 'author', 'created_at', 'category') 
#     search_fields= ('title', 'content') 
#     list_filter= ('category', 'created_at')
