from typing import List

from django.urls import path

from . import views

app_name: str = "core"


urlpatterns: List = [
    path("", views.IndexView.as_view(), name="index"),
]
