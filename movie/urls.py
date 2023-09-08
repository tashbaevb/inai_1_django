from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('movie/', views.movie_all, name='movie'),
    path('movie/<int:id>', views.movie_more, name='more'),
    path('movie/<int:id>/update/', views.movie_update, name='movie_update'),
    path('movie/<int:id>/delete/', views.movie_delete, name='movie_delete'),
    path('add-movie/', views.add_movie, name='add_movie'),

   ]

