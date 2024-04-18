from django.contrib import admin
from .models import Job
from .models import Price_oofer

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','description','position','created_at')

admin.site.register(Price_oofer)