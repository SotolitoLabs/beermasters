from django.urls import path
from . import views

# TODO: fix URL's to make semantic sense
urlpatterns = [
    # Competitions
    path('', views.index, name='index'),
    path('add', views.competition, name='index'),
    path('<int:contest_id>/', views.detail, name='detail'),
    #path('<int:contest_id>/scoresheet', views.scoresheet, name='scoresheet'),
    path('<int:table_item_id>/score', views.score, name='score'),

    # Tables
    path('table/<int:table_id>', views.table, name='table'),
    path('table/<int:table_id>/item/scoresheet/<int:item_id>', views.scoresheet, name='scoresheet'),

    # Users
    path('register/', views.register, name='register'),
    path('profile/<int:user_id>', views.profile, name='profile'),

    # Breweries
    path('brewery/<int:brewery_id>', views.brewery_detail, name='brewery_detail'),
    path('brewery/add', views.brewery, name='brewery'),
    path('breweries/', views.breweries, name='breweries'),

    # Beers
    path('beers/', views.beers, name='beers'),
    path('beer/<int:beer_id>', views.beer_detail, name='beer_detail'),
    path('beer/add', views.beer, name='beer'),
]
