from django.contrib import admin
from .models import Recepta, Ingredient, Mesura, Comentari, ReceptaIngredient

#admin.site.register(Recepta)
#admin.site.register(Ingredient)
admin.site.register(Mesura)
admin.site.register(Comentari)
#admin.site.register(ReceptaIngredient)


class IngredientInline(admin.TabularInline):
    model = ReceptaIngredient
    extra = 0
    ordering = ['ingredient']

# Define the admin class
class ReceptaAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_creacio', 'data_consumit', 'actiu')
    list_filter = ('data_creacio', 'data_consumit', 'actiu', 'dificultat', 'thermomix')
    fields = ['title', 'descripcio', ('dificultat', 'temps_preparacio','temps_total','racions'),('actiu','thermomix')]
    inlines = [IngredientInline]

# Register the admin class with the associated model
admin.site.register(Recepta, ReceptaAdmin)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
    
@admin.register(ReceptaIngredient)
class ReceptaIngredientAdmin(admin.ModelAdmin):
    pass
    
