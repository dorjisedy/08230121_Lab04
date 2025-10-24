from django.contrib import admin
from .models import LearningJourney, AboutMe

# Register the model to make it visible in Django admin panel
admin.site.register(LearningJourney)
admin.site.register(AboutMe)


