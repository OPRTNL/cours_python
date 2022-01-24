from django.contrib import admin
from .models import Pizza
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegan', 'prix')
    search_fields = ['nom']

admin.site.register(Pizza, PizzaAdmin)