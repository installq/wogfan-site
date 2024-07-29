from django.contrib import admin

# Register your models here.

from .models import Record, Record2, Level, Level2, Player

admin.site.register(Record)
admin.site.register(Record2)
admin.site.register(Level)
admin.site.register(Level2)
admin.site.register(Player)
