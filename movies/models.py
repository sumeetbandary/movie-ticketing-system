from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=100)
    screen = models.CharField(max_length=100, default="Screen 1")
    show_times = models.TimeField(default=timezone.make_aware(
        timezone.datetime(2023, 1, 1, 20, 0)))


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    availability = models.BooleanField(default=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    date = models.DateField()
