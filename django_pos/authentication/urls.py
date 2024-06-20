from django.urls import path
from .views import login_view, register_user, logout_view, profile, index, UserCreateView

app_name = "authentication"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("", index, name="users_index"),
]
