from django.shortcuts import render
from .models import Topic, AboutMe

# Home page view
def index(request):
    topics = Topic.objects.prefetch_related('challenges').all()
    return render(request, 'index.html', {'topics': topics})

# About Me page view
def about_me(request):
    about = AboutMe.objects.prefetch_related('hobbies', 'skills').first()
    return render(request, 'aboutMe.html', {'about': about})
