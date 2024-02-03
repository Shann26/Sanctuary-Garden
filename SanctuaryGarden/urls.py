from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import addplant

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about/', views.about_page, name="about_page"),
    path('login/', views.login_page, name="login_page"),
    path('collection/', views.collection_page, name="collection_page"),
    path('PlantCareGuide/<int:id>/', views.PlantCareGuide_page, name="PlantCareGuidePage"),
    path('category/', views.category_page, name="category_page"),
    path('Collection/<int:id>/', views.done, name="done"),
    path('AddPlant/', addplant, name="addplant_page"),
    path('AddPlants/', views.addplants, name="addplants"),
    path('deleteplant/<int:id>/',views.deleteplant, name='deleteplant'),
    path('editplantpage/<int:id>/',views.editplantpage, name='editplantpage'),
    path('editplant/<int:id>/', views.editplant, name='editplant'),
    path('administrator/', views.administrator_page, name="administrator"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
