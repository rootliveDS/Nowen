from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
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

##Api
############################################################################################################
############################################################################################################
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

#
# ####Work then
# ####################################
# # class UserPage(CreateView):
# #     def dispatch(self, request):
# #         if not request.user.is_authenticated():
# #             return HttpResponseForbidden()
# #         return super(UserPage, self).dispatch(request)
#
# class UserPage(CreateView):
#     queryset = Post.objects.filter.author()
#     serializer_class = PostSerializer
#
#     def dispatch(self, request, *args, **kwargs):
#
#         active_user = request.user.get_username()
#         if active_user == request.user.is_authenticated():
#             return render(request, 'nowen/profile.html')
#
# # class UserPost(generics.CreateAPIView):
# #     permission_classes = (IsAuthorOrReadOnly,)
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# #     def dispatch(self, request):
# #         user = request.user.is_authenticated()
#
#
#
#     # if Post.objects.filter(user=username):
#     #    return render(request, 'nowen/profile.html')
########################################################################
########################################################################

########################################################################
########################################################################
# class UserPage(SingleObjectMixin, View):
#     model = Post
#     def post(self,request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         return render(request, 'nowen/profile.html')
#
# class UserPage(SingleObjectMixin, View):
#     model = Post
#     def post(self,request, *args, **kwargs):
#         active_user = request.user.is_authenticated.id
#         if Post.objects.filter(author=active_user):


# class UserPage(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# def UserPage(request):
#     context = {
#         'posts': Post.objects.filter(author=request.user)
#     }
#     return render(request, 'nowen/profile.html', context)

# class UserList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer

########################## IT,s Work
########################################################################
################################################################################################################################################
########################################################################

class UserPage(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)