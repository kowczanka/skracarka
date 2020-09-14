from django.db import models

# Create your models here.

class Link(models.Model):
    target = models.TextField()
    count = models.IntegerField(default=0)   #dodajemy kolejny wiersz do bazy, który bedzie zliczał ilość kliknięć na link.
                                             # te podmioty które dodalismy do tej pory nie mają tego pola, więc dodajemy default = 0
    last_visited = models.DateTimeField(auto_now=True)