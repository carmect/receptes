from django.contrib import admin
from .models import Recepta, Ingredient, Mesura, Comentari, ReceptaIngredient, Categoria, Passa

#admin.site.register(Recepta)
admin.site.register(Ingredient)
admin.site.register(Mesura)
admin.site.register(Comentari)
admin.site.register(Categoria)
#admin.site.register(ReceptaIngredient)


class IngredientInline(admin.TabularInline):
    model = ReceptaIngredient
    extra = 0
    ordering = ['ingredient__nom']
    
class PassaInline(admin.TabularInline):
    model = Passa
    extra = 0
    
class ComentariInline(admin.TabularInline):
    model = Comentari
    extra = 0
    
class CategoriaInline(admin.TabularInline):
    model = Recepta.categories.through
    extra = 0
    ordering = ['categoria__nom']

# Define the admin class
class ReceptaAdmin(admin.ModelAdmin):
    list_display = ('titol', 'data_creacio', 'data_consumit', 'actiu')
    list_filter = ('data_creacio', 'data_consumit', 'actiu', 'dificultat', 'thermomix')
    fields = ['titol', 'descripcio', 'foto', ('dificultat', 'temps_preparacio','temps_total','racions'),('actiu','thermomix')]
    inlines = [IngredientInline, PassaInline, CategoriaInline, ComentariInline]

# Register the admin class with the associated model
admin.site.register(Recepta, ReceptaAdmin)


