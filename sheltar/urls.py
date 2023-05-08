
from django.contrib import admin
from django.urls import path
from core.views import index, about, properties, sheltarGO, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('properties/', properties, name='properties'),
    path('sheltarGO/', sheltarGO, name='sheltarGO'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
