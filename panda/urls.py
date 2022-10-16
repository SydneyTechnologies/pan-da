from django.urls import path
from . views import searchMovie, getMovie, LoginView, CreateUserView

urlpatterns = [
    path('signup', view = CreateUserView.as_view(), name ="create"),
    path('token', view = LoginView.as_view(), name="login"),
    path('search/<str:search>', view = searchMovie, name="search"),
    path('get/<str:link>', view = getMovie, name="get"),
]
