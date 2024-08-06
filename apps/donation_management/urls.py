from django.urls import path, include
from . import views

urlpatterns = [
    path("create-project-donation/", views.create_donation, name="create_donation"),
    path("get-all-project-donations/", views.GetAllDonations.as_view(), name="get_all_donations",),
    path("get-all-waqf-donations/", views.GetAllWaqfDonations.as_view(), name="get_all_waqf_donations",),
]
