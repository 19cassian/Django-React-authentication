
from django.urls import path
from .import views


urlpatterns = [
    path('signup/', views.createUserView, name="signup"),
    path('users/', views.Users_list, name="signup"),



]