from django.contrib import admin
from .models import Raza



class RazaAdmin(admin.ModelAdmin):
    list_display = ["raza",]
    class Meta: Raza

admin.site.register(Raza, RazaAdmin)
