from django.shortcuts import render, redirect
import sys
sys.path.append('path/to/module')
import datetime
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Movie, Seat, Booking
from .form import MovieForm
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ticketing/movie_list.html', {'movies': movies})


def seat_selection(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(availability=True)
    return render(request, 'ticketing/seat_selection.html', {'movie': movie, 'seats': seats})


def book_ticket(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    seat.availability = False
    seat.save()
    booking = Booking.objects.create(
        user=request.user, movie=movie, seat=seat, date=datetime.datetime.now().date())
    return render(request, 'ticketing/booking_confirmation.html', {'booking': booking})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})
