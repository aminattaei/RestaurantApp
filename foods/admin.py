from django.contrib import admin
from .models import Food

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'rate', 'price','type_food')  
    search_fields=['rate','price']
    def get_types(self, obj):
        return ", ".join([type.name for type in obj.types.all()])  
    get_types.short_description = 'نوع غذاها'  

admin.site.register(Food, FoodAdmin)
# admin.site.register(FoodType)
    
    
    

