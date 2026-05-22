
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('create/',views.post_tasks),
    path('update/<int:id>/',views.update_tasks),
    path('partial/<int:id>/',views.patch_tasks)
]