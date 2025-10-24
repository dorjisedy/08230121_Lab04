from django.db import models

# ================================
# Model 1: Learning Journey
# ================================
class LearningJourney(models.Model):
    """
    Represents each learning milestone or experience in your journey.
    """
    title = models.CharField(max_length=100)  # Title of the milestone
    description = models.TextField()          # What you learned
    date = models.DateField()                 # Date of learning

    def __str__(self):
        return self.title


# ================================
# Model 2: About Me
# ================================
class AboutMe(models.Model):
    """
    Stores basic personal details about yourself.
    """
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    interests = models.TextField()
    hobbies = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About Me"
    

