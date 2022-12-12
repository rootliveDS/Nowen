from django.urls import path, include, re_path
from .views import PostList, PostDetail, SignUp, UserList, UserDetail, StartPage, UserPage


urlpatterns = [
    path('', StartPage, name='home'),
    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/post/<int:pk>/', PostDetail.as_view()),
    path('api/post', PostList.as_view()),
    path('accounts/signup/', SignUp.as_view()),
    re_path('^profile/(?P<username>.+)/$', UserPage.as_view()),
]


# <str:username>/
