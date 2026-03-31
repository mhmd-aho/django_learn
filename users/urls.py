from django.urls import path
from . import views


urlpatterns = [
    path('', views.usersList),
    path('register/', views.register),
    path('<int:id>/', views.userById),
]