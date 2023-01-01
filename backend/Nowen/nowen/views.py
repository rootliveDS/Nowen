from rest_framework import generics
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication

##################################################################
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
##################################################################

def StartPage(request):
    return render(request, 'nowen/index.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

##############################

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

##############################

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

##############################

class UserPage(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        profile = self.request.user
        if profile is not None:
            queryset = queryset.filter(author__username=profile)
            return queryset
