from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    github = models.URLField(max_length=500, null=False, blank=False)
    linkedin = models.URLField(max_length=500, null=False, blank=False)
    bio = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
