from django.urls import path
from . import views

# URL configuration for users app.
urlpatterns = [
    path('hello/', views.say_hello),
]
