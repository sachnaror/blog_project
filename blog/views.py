from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import BlogPost, CustomUser


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pin = request.POST.get('pin')
        user = authenticate(request, username=email, password=pin)
        if user is not None and user.mobile == mobile:
            login(request, user)
            return redirect('blog_list')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login.html')

@login_required
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})
