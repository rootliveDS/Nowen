from django.urls import path, include
from .views import PostList, PostDetail, SignUp

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('accounts/signup/', SignUp.as_view()),
]