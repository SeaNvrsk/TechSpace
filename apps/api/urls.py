from django.urls import path, re_path
from apps.api import views

urlpatterns = [
    path('user/settings/update', views.updateUserSettings),
]
