from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contest_id>/', views.detail, name='index'),
    #path('<int:contest_id>/', views.delete, name='index', method="DELETE"),
    #path('<int:contest_id>/', views.delete, name='index', method="POST"),
    #path('<int:contest_id>/', views.delete, name='index', method="PUT"),
    #path('<int:contest_id>/', views.delete, name='index', method="GET"),
]

