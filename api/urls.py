
from django.urls import path
from .views import createUserView
from .import views
urlpatterns = [
    path('signup/', views.createUserView, name="signup"),

]