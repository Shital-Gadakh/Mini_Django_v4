from django.urls import path, include
from jobs import views

urlpatterns = [

    path(r"^wel*", views.welcome),
    path("portal/", views.portal_details)

]
