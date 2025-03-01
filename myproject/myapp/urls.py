from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication Routes
    path('register/', views.register, name='register'),  # Signup URL
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL

    # CRUD Operations
    path('', views.home, name='home'),  # Home page
    path('adduser/', views.add_user, name='add_user'),
    path('updateuser/<int:id>/', views.update_user, name='update_user'),
    path('deleteuser/<int:id>/', views.delete_user, name='delete_user'),
]




