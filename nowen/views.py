from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer, UserListSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# import functools


def StartPage(request):
    return render(request, 'nowen/index.html')

def UserPage(request, username):
    return render(request, 'nowen/index.html')

# def PostMain(self, request):
#    username = self.request.user
#    if Post.objects.filter(user=username):
#        return render(request, 'nowen/profile.html')

# class PostMain(generics.ListAPIView):
#     serializer_class = UserListSerializer
#     def get_queryset(self):
#         Post.objects.filter(author=request.user)
#         return Post.objects.filter(user=username)


def PostMain(request):
    author = Post.objects.all()
    user_id = request.user.id
    if user_id == author:
        return render(request, 'nowen/profile.html' )

class Ad(generics.ListCreateAPIView):
    queryset = Post.objects.all()

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer