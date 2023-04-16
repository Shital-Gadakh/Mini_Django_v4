from django.urls import path, include
from unicodedata import name

from jobs import views

urlpatterns = [

    path(r"^wel*", views.welcome, name="welcome"),
    path("portal/", views.portal_details, name="portal_details"),
    path("<int:job_id>/", views.job_description, name="JD")   # http://127.0.0.1:8000/jobs/55/
]
##########################################################
# How to capture path parameter from url         #
##########################################################
# Notes:
#
# To capture a value from the URL, use angle brackets.
# Captured values can optionally include a converter type.
# For example, use <int:name> to capture an integer parameter.
# If a converter isn’t included,
# any string, excluding a / character, is matched.
# There’s no need to add a leading slash, because every URL has that.
# For example, it’s articles, not /articles.
##########################################################
