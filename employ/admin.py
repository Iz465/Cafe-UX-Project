from django.contrib import admin
from . models import Employ

class EmployAdmin(admin.ModelAdmin):
  list_display = ('name', 'income')

admin.site.register(Employ,EmployAdmin)



