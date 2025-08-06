
from django.urls import path

from accounts import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("news", views.news, name="news"),
    path("destinations", views.destinations, name="destinations"),
]
