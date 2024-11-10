from django.contrib import admin
from .models import Blog,Category



# admin.site.register(Blog)
admin.site.register(Category)


# class CategoryInline(admin.TabularInline):
#     model = Category
#     fields=['title','slug','published_at']
#     extra=0
    
    
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','description','created_time','author']
    search_fields=['title','author']
    # inlines=[CategoryInline]



    

