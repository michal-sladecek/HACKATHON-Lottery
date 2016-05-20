from django.contrib import admin
from .models import LoteriaModel,UserData,PodanyTicketModel, NakupnyPlan

@admin.register(LoteriaModel)
class LoteriaModelAdmin(admin.ModelAdmin):
    pass

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass

@admin.register(PodanyTicketModel)
class PodanyTicketModelAdmin(admin.ModelAdmin):
    pass

@admin.register(NakupnyPlan)
class NakupnyPlanModelAdmin(admin.ModelAdmin):
    pass