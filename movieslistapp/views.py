from django.shortcuts import render
from .models import movies_info

def movies_list(request):
    movies = movies_info.objects.all()
    movies_list = []
    for movie in movies:
        movies_list.append ({'movie':movie})
    
    context = {'movies_list': movies_list}
    return render(request , 'movieslistapp/movies_list.html' , context)