from django.urls import path
from . import views

urlpatterns = [

    # ログインページ
    path("", views.LoginPage.as_view(), name="login"),

    # ログイン完了ページ
    path("home", views.HomePage.as_view(), name="home"),
]