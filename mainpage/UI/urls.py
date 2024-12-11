from django.urls import path
from . import views
from UI import views as accounts_views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')), 
    path('home/', views.home_view, name='homepage'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('complaint/', views.complaint_view, name='complaint'),
    path('compliment/', views.compliment_view, name='compliment'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
