import imp
from django import urls
from django.urls import path, re_path

from .views import Dash, PostVideos

urlpatterns = [
    re_path(r'search', Dash.as_view(), name="search"),
    re_path(r'index', PostVideos.as_view(), name="index"),
]
