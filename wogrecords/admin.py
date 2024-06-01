from django.contrib import admin

# Register your models here.

from .models import Record, Level, Player

admin.site.register(Record)
admin.site.register(Level)
admin.site.register(Player)