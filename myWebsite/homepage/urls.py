from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs_detail/', views.blog_detail, name='blog_detail'),
]
