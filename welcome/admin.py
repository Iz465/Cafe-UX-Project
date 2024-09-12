from django.contrib import admin
from .models import Welcome


class WelcomeAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')


admin.site.register(Welcome, WelcomeAdmin)


