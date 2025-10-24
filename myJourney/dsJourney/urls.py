from django.urls import path
from . import views

# Define routes for your app
urlpatterns = [
    # Homepage showing learning journey
    path('', views.index, name='index'),
    
    # About Me page showing personal information
    path('about/', views.aboutMe, name='aboutMe'),
]
