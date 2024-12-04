from django.urls import path
from . import views

urlpatterns = [
    path("requests/", views.get_all_requests, name="get_all_requests"),
    path("responses/", views.get_all_responses, name="get_all_responses"),
]
