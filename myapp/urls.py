from django.urls import path
from .views import *
# from.import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='index'),
    path ("contact/", contact, name='contact'),
    path('post_list', post_list, name="post_list"),
    # path('create_post', views.create_post)
       ]

urlpatterns += staticfiles_urlpatterns()