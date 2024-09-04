from blog import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),

]
