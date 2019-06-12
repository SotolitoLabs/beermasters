from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contest_id>/', views.detail, name='detail'),
    path('<int:contest_id>/scoresheet', views.scoresheet, name='scoresheet'),
]
