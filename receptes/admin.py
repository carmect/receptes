from django.contrib import admin
from .models import Recepta, Ingredient, Mesura, Comentari, ReceptaIngredient

#admin.site.register(Recepta)
admin.site.register(Ingredient)
admin.site.register(Mesura)
admin.site.register(Comentari)
#admin.site.register(ReceptaIngredient)


class IngredientInline(admin.TabularInline):
    model = ReceptaIngredient
    extra = 0
    ordering = ['ingredient__nom']
    
class ComentariInline(admin.TabularInline):
    model = Comentari
    extra = 0

# Define the admin class
class ReceptaAdmin(admin.ModelAdmin):
    list_display = ('titol', 'data_creacio', 'data_consumit', 'actiu')
    list_filter = ('data_creacio', 'data_consumit', 'actiu', 'dificultat', 'thermomix')
    fields = ['titol', 'descripcio', 'foto', ('dificultat', 'temps_preparacio','temps_total','racions'),('actiu','thermomix')]
    inlines = [IngredientInline, ComentariInline]

# Register the admin class with the associated model
admin.site.register(Recepta, ReceptaAdmin)


    
    
