from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contest_id>/', views.detail, name='detail'),
    #path('<int:contest_id>/scoresheet', views.scoresheet, name='scoresheet'),
    path('<int:contest_id>/score', views.score, name='score'),
    path('table/<int:table_id>', views.table, name='table'),
    path('table/<int:table_id>/item/scoresheet/<int:item_id>', views.scoresheet, name='scoresheet'),
]
