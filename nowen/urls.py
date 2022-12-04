from django.urls import path, include
from .views import PostList, PostDetail, SignUp, UserList, UserDetail, StartPage

urlpatterns = [
    path('', StartPage, name='home'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/post/<int:pk>/', PostDetail.as_view()),
    path('api/post', PostList.as_view()),
    path('accounts/signup/', SignUp.as_view()),
]