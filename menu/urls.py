from django.urls import path
from .views import index, listMenuPage


urlpatterns = [
  path('', index, name = "menu"),
  path("listmenu",listMenuPage,name="MenuItems")
 
]