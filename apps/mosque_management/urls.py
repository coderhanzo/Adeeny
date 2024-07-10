from django.urls import path, include
from . import views


urlpatterns = [
  path("create-mosque/", views.create_mosque, name="create_mosque"),
]