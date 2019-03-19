from django.db import models
from django.utils import timezone

class Recepta(models.Model):
    title = models.CharField(max_length=200)
    descripcio = models.TextField()
    data_creacio = models.DateTimeField(
            default=timezone.now)

    data_programat = models.DateTimeField(
            blank=True, null=True)

    data_consumit = models.DateTimeField(
  	    blank=True, null=True)

    actiu = models.BooleanField(default=True)

    def activa(self):
        self.actiu = True
        self.save()

    def desactiva(self):
        self.actiu = False
        self.save()

    def consumeix(self):
        self.data_consumit = timezone.now
        self.data_programat = timezone.null
        self.save()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

        
class Mesura(models.Model):
    nom = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom
        
class Comentari(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE, related_name='comentaris')
    autor = models.CharField(max_length=200)
    text = models.TextField()
    data_creacio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text