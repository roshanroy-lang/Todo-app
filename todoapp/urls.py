
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('create/',views.post_tasks)
]