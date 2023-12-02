# from django.db import models
# from django.utils.text import slugify
# from django.contrib.auth.models import User
# from django.urls import reverse
# from cloudinary.models import CloudinaryField
# # Create your models here.



# class Category(models.Model):
#     name = models.CharField(max_length=50, null=True, unique=True)
#     slug=models.SlugField(max_length=50, null=True, unique=True)
    

#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         self.slug=slugify(self.name)
#         super().save(*args, **kwargs)

# class Post(models.Model):           
#          name = models.CharField(max_length=100, unique=True)
#          slug =models.SlugField(max_length=50, unique=True)
#          author= models. ForeignKey(User, on_delete=models.CASCADE)
#          content= models.TextField()
#          post_image= CloudinaryField('post_image', null=True, blank=True)
#          created_at = models.DateTimeField(auto_now_add=True)
#          updated_at =models.DateTimeField(auto_now=True)
#          category =models.ForeignKey(Category, on_delete=models.CASCADE)
# def __str__(self):
#              return self.title
# def get_absolute_url(self):
#             return reverse('post_detail', args=[str(self.slug)])


# def save(self, *args, **kwargs):
#             self.slug=slugify(self.title)
#             super().save(*args, **kwargs)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.title