from django.urls import path, include

from . import views

urlpatterns = [
    path("logout/", views.logout_view, name='logout'),
    path("login/", views.Login.as_view(), name='login'),
    path("singup/", views.Singup.as_view(), name='singup'),
    path("profile/", views.profile, name='profile'),
    path("documents/", views.DocumentView.as_view(), name='documents'),
    path("add_post/", views.PostAuction.as_view(), name='addpost'),
]
