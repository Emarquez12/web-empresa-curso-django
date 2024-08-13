from django.shortcuts import render, get_object_or_404

from blog.models import Category, Post

# Create your views here.

def blog(request):
    
    blog = Post.objects.all()
    
    return render(request,"blog/blog.html", {'blog': blog})  


def category(request, category_id):
    category = get_object_or_404(Category,id=category_id)
    #blog = Post.objects.filter(categories=category)
    return render(request,"blog/category.html",{'category': category}) 
    