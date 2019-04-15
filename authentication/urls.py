from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('def_login/', views.default_login_view, name="def_login"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]