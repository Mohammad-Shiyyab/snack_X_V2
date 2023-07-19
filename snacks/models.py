from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Snack(models.Model):
    name=models.CharField(max_length=255,help_text='isert the title of snacks')
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description =models.TextField(blank=True)

    def __str__ (self):
       return self.name
    def get_absolute_url(self):
        return reverse ('snack_list')