from django.db import models
    

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    progress = models.CharField(max_length=200)
    notes = models.CharField(max_length=1000)



