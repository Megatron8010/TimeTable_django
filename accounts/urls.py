from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from . import views
# from django.contrib.auth import views as auth_views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('home/',views.indexView, name="home"),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.registerView,name="register_url"),
    path('create/', views.CreateMovieView.as_view(), name='create'),
    path('update/', views.UpdateMovieView.as_view(), name='update'),
    # path('api-auth/urls', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-auth', include(router.urls)),
    # path('get_username/',views.my_view,name="get_username"),
    # path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    
    
    path('login/',views.loginView,name="signin")


]
