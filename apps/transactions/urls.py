from django.urls import path
from . import views


urlpatterns = [
  path("payments/", views.PaymentsView.as_view()),
  path("collections/", views.CollectionsView.as_view()),
  path("callback/", views.PaymentCallbackAPIView.as_view()),
]