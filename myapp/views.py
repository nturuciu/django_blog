from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def post_list(request):
    posts = Post.objects.all(all)
    return render(request, "post_list.html", {"post": posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.Files)

        if form.is_valid():
            post = form.save(commit=False)

            post.save()

            form = POSTFORM()

            return redirect("/post_list")
        else:
            form = PostForm

            return render(request, "post_form.html", {"form": form})


def edit_post(request):
    post = Post.objects.get()

    form = EditPostForm(instance=post)
    if request.method == "POST":
        form = EDITPOSTFORM(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect("/post_list")
