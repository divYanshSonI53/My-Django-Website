from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'home/homepage.html')

def blogs(request):
    return render(request, 'blogs/blog_grids.html')

def blog_detail(request):
        return render(request, 'blogs/blog_details.html')

