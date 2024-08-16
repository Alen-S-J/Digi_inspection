from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('overview/', views.overview_view, name='overview'),
    path('newproject/', views.newproject_view, name='newproject'),
    path('success/', views.success, name='success'),

    
]
