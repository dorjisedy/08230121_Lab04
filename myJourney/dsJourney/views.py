from django.shortcuts import render

# Create your views here.
from .models import LearningJourney, AboutMe

# View function to display all learning journey records
def index(request):
    # Retrieve all records from the LearningJourney model
    journeys = LearningJourney.objects.all()
    
    # Render index.html template with journey data
    return render(request, 'index.html', {'journeys': journeys})

# View function to display personal details
def aboutMe(request):
    # Retrieve all AboutMe records so the template can display multiple profiles
    abouts = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'abouts': abouts})

