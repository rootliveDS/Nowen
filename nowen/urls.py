from django.urls import path, include
from .views import PostList, PostDetail, SignUp, UserList, UserDetail, StartPage, UserPage, PostMain

##################
# <str:username>/
#
#


urlpatterns = [
    path('', StartPage, name='home'),
    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/post/<int:pk>/', PostDetail.as_view()),
    path('api/post', PostList.as_view()),
    path('accounts/signup/', SignUp.as_view()),
    path('profile/<str:username>/', UserPage, name='profile'),
    path('test/', PostMain, name='context'),
]
