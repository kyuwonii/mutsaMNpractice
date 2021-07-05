from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie(request):
    movies=Movie.objects
    return render(request, 'movie/movie.html',{'movies':movies})