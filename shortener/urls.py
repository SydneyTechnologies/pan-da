from django.urls import path
from . import views

urlpatterns = [
    path("vids/<str:link>", view=views.ShortenLink.as_view(), name="shorten")
]
