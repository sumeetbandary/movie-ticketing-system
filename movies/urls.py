from django.urls import path
from .views import (
    movie_list,
    seat_selection,
    book_ticket,
    add_movie,
)

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_selection, name='seat_selection'),
    path('movies/<int:movie_id>/seats/<int:seat_id>/book/',
         book_ticket, name='book_ticket'),
    path('admin/movies/add/', add_movie, name='add_movie'),
]
