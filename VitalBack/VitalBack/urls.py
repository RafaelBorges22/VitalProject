from django.contrib import admin
from django.urls import path  # Esta importação estava faltando
from Motorist.API.viewset import MotoristViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include 

router = DefaultRouter()
router.register('motorist', MotoristViewSet, basename='motorist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Adicione também a importação de include se necessário
]