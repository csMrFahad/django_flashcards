from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create-set', views.create_set, name='create_set'),
    path('view-set', views.view_set, name='view_set'),
]
