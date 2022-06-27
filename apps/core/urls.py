from django.urls import path, re_path
from apps.core import views

urlpatterns = [

    # The home page
    path('', views.indexView, name='home'),
    path('profile', views.profileView, name='profile'),
    path('billing', views.billingView, name='billing'),
    path('tables', views.tablesView, name='tables'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pagesView, name='pages'),

]
