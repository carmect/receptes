﻿from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    mesura = models.ForeignKey('receptes.Mesura', on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom',]),
            ]

    def __str__(self):
        return self.nom + " (" + self.mesura.nom + ")"
        
        
class Categoria(models.Model):
    nom = models.CharField(max_length=40, unique=True)
    
    class Meta:
        ordering = ['nom']
        verbose_name_plural = u'Categories'
        
    def __str__(self):
        return self.nom
        
        
class Recepta(models.Model):
    titol = models.CharField(max_length=200)
    descripcio = models.TextField()
    foto = models.ImageField(upload_to = 'fotos/', default = '/no-img.jpg')
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

    categories = models.ManyToManyField(Categoria)
    
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
        
    class Meta:
        indexes = [
            models.Index(fields=['titol',]),
            #models.Index(fields=['descripcio',]),
            ]
        verbose_name_plural = u'Receptes'
            
    def __str__(self):
        return self.titol

        
class Mesura(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    
    class Meta:
        ordering = ['nom']
        verbose_name_plural = u'Mesures'
    
    def __str__(self):
        return self.nom
        
        
class Comentari(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE, related_name='comentaris')
    titol = models.CharField(max_length=200)
    text = models.TextField()
    data_creacio = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.titol
        
        
class ReceptaIngredient(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('receptes.Ingredient', on_delete=models.CASCADE, related_name='receptes')
    quantitat = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.recepta.titol + " - " + self.ingredient.nom

        
class Passa(models.Model):
    recepta = models.ForeignKey('receptes.Recepta', on_delete=models.CASCADE, related_name='passes')
    descripcio = models.CharField(max_length=200,default='')
    ordre = models.PositiveSmallIntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ['recepta__titol','ordre']
        verbose_name_plural = u'Passes'
        
    def __str__(self):
        return self.recepta.titol + " - " + str(self.ordre)
        