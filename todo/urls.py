from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    # Login ke liye built-in view
    path('login/', LoginView.as_view(template_name='todo/login.html'), name='login'),
    # Signup ke liye aapka banaya hua view
    path('signup/', views.signup, name='signup'), 
]