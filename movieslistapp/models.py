from django.db import models

class movies_info(models.Model):
    name = models.CharField(max_length=100 , help_text="the name of the movie.")
    date = models.DateField(verbose_name="date the movie was released.")