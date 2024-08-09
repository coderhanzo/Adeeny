from django.urls import path, include
from . import views


urlpatterns = [
    path("create-mosque/", views.create_mosque, name="create_mosque"),
    path("get-all-mosques/", views.GetAllMosques.as_view(), name="get_all_mosques"),
    path("update-mosque/", views.GetAndUpdateMosque.as_view(), name="update_mosque"),
    path("get-all-liked-mosques/", views.get_liked_mosques),
    path("create-annoucment/", views.create_announcement, name="create_annoucment"),
    path("get-all-annoucments/", views.get_all_announcements, name="get_all_annoucments",),
    path("update-annoucment/",views.GetAndUpdateMosque.as_view()),
]
