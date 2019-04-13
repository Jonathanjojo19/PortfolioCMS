from django.urls import path
from . import views

app_name = "cms"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('update-info/', views.updateInfo, name="updateInfo"),
    path('update-project/', views.updateProject, name="updateProject"),
]