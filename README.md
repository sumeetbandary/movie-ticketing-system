# Django Movie Ticketing App

This is a movie ticketing app built using Django as a backend framework.

## Features

- Two types of users: admin and general user
- Admin can add and delete movies
- General users can select a movie and book a ticket
- Multiple movies available
- One screen present
- Seats displayed when a movie is selected
- Book a seat for a selected movie

## Requirements

- Python 3.x
- Django
- Other dependencies listed in the `Pipfile` file

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a virtual environment: `python -m venv myenv`
4. Activate the virtual environment: `source myenv/bin/activate`
5. Apply database migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Access the application at `http://127.0.0.1:8000/`


## Routes

1. `/admin/` - This is the Django admin panel route, where the admin can manage the movies and tickets.
2. `/` - This is the home page route, where users can see the list of movies available.
3. `/movies/` - List all the movies available.
3. `/admin/movies/add/` - Admin can add the movie.
4. `/movies/<int:movie_id>/seats/` - Select a seat.
3. `/movies/<int:movie_id>/seats/<int:seat_id>/book/>` - Users can can book the selected seat for a movie.
