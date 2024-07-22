from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "create-project-donation/", views.create_project_donation, name="create_donation"
    ),
    path("get-all-project-donations/", views.GetAllProjectDonation.as_view(), name="get_all_donations"),
]
