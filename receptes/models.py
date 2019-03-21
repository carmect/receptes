from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    nom = models.CharField(max_length=50)
    mesura = models.ForeignKey('receptes.Mesura', on_delete=models.PROTECT)

    def __str__(self):
        return self.nom + " (" + self.mesura.nom + ")"
        

class Recepta(models.Model):
    title = models.CharField(max_length=200)
    descripcio = models.TextField()
    data_creacio = models.DateTimeField(
            default=timezone.now, editable=False)

    data_programat = models.DateTimeField(
            blank=True, null=True, editable=False)

    data_consumit = models.DateTimeField(
  	    blank=True, null=True, editable=False)

    actiu = models.BooleanField(default=True)
    
    thermomix = models.BooleanField(default=True)
    
    DIFICULTAT_CHOICES = (
        ('F', 'Fàcil'),
        ('M', 'Mitjana'),
        ('D', 'Difícil'),
    )
    dificultat = models.CharField(
        max_length=1,
        choices=DIFICULTAT_CHOICES,
        default='F'
    )
    
    temps_preparacio = models.CharField(
        max_length=7,
        blank=True, null=True,
    )
    
    temps_total = models.CharField(
        max_length=7,
        blank=True, null=True,
    )
    
    racions = models.PositiveSmallIntegerField(
        blank=True, null=True)
    
    ingredients = models.ManyToManyField(
        Ingredient,
        through='ReceptaIngredient',
    )

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

        
class Mesura(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nom
        
        
class Comentari(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE, related_name='comentaris')
    titol = models.CharField(max_length=200)
    text = models.TextField()
    data_creacio = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.text
        
        
class ReceptaIngredient(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('receptes.Ingredient', on_delete=models.CASCADE, related_name='receptes')
    quantitat = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.recepta.title + " - " + self.ingredient.nom
    