from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = "base"

urlpatterns = [
    path('', include('report.urls')),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.fullUserCreateForm, name='sign_up'),
    # path('personal/', views.UserPersonalPage.as_view(), name='personal'),
    path('personal/<str:username>', views.userPage, name='personal'),
    path('personal/<str:username>/comments', views.user_page_comments, name='comments'),
    path('personal/<str:username>/likes', views.user_page_likes, name='likes'),
]
