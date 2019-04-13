from django.urls import path
from . import views

app_name = "cms"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('update-info/', views.update_info, name="update_info"),
    path('update-project/', views.update_project, name="update_project"),
]