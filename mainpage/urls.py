"""
URL configuration for mainpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UI import views as accounts_views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ui/', include('UI.urls')),
    path('', lambda request: redirect('login')),
    path('admin-login/',accounts_views.admin_login, name='admin_login'),
    path('admin-dashboard/', accounts_views.admin_dashboard, name='admin_dashboard'),
    path('accounts/home/', accounts_views.home_view, name='home'), 
    path('accounts/signup/', accounts_views.signup, name='signup'),  
    path('accounts/login/', auth_views.LoginView.as_view(template_name='UI/login.html'), name='login'), 
    path('accounts/login/', auth_views.LogoutView.as_view(), name='logout'),  
]
