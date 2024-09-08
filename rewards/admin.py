from django.contrib import admin
from .models import Rewards, Offer


class RewardsAdmin(admin.ModelAdmin):
  list_display = ('name','points')

class OffersAdmin(admin.ModelAdmin):
  list_display = ('code','discount')



admin.site.register(Rewards, RewardsAdmin)
admin.site.register(Offer, OffersAdmin)

