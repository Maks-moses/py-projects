from django.contrib import admin
from django.contrib.auth.models import Permission
from listings.models import Band
from listings.models import Title

class BandAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_de_creation', 'genre')

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Title, TitleAdmin)
