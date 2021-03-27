from django.urls import path
from . import views

urlpatterns = [
    path('<permalink>', views.index, name="about"),
]
