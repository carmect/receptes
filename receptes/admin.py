from django.contrib import admin
from .models import Recepta, Ingredient, Mesura, Comentari

admin.site.register(Recepta)
admin.site.register(Ingredient)
admin.site.register(Mesura)
admin.site.register(Comentari)