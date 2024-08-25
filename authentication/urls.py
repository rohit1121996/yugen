from django.urls import path

from . import views

app_name = "auth"
urlpatterns = [
    path("callback", views.callback, name="callback"),
    path("logout", views.logout_user, name="logout"),
]
