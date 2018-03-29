from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from users.models import UserModel
from users.forms import RegisterForm
# Create your views here.


def register(request):
    request_form=RegisterForm(request.POST)
    if request_form.is_valid():
        post=request.POST
        user_name=post.get('user_name','')
        pass_word1=post.get('pass_word1','')
        pass_word2=post.get('pass_word2','')
        if pass_word1 != pass_word2:
            return render(request,'users/register.html')
        email=post.get('email','')
        users=UserModel()
        users.username=user_name
        users.password=make_password(pass_word2)
        users.email=email
        users.save()
        return render(request,'index.html')
    else:
        return render(request,'users/register.html')