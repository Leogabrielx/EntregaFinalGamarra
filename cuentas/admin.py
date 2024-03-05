from django.contrib import admin
from .models import InfoExtra
# Register your models here.

@admin.register(InfoExtra)
class InfoExtraAdmin(admin.ModelAdmin):
    search_fields = ('user', 'es_admin', 'link')
    list_display = ('user', 'es_admin', 'link', 'avatar')
