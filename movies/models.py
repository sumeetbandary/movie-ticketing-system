from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    show_times = models.TimeField()

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    availability = models.BooleanField(default=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    date = models.DateField()
