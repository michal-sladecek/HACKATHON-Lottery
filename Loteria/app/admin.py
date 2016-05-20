from django.contrib import admin
from .models import LoteriaModel,UserData,PodanyTicketModel

@admin.register(LoteriaModel)
class LoteriaModelAdmin(admin.ModelAdmin):
    pass

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass

@admin.register(PodanyTicketModel)
class PodanyTicketModelAdmin(admin.ModelAdmin):
    pass