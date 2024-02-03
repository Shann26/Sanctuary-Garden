from django.contrib import admin
from .models import Profile, PlantCareGuide, Category, CategoryBridge, Collection

admin.site.register(Profile)
admin.site.register(PlantCareGuide)
admin.site.register(Category)
admin.site.register(CategoryBridge)
admin.site.register(Collection)