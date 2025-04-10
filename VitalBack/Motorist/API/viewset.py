# Motorist/API/viewset.py
from rest_framework import viewsets
from .serializers import MotoristSerializer  # Importação relativa correta
from Motorist.models import MotoristModel  # Caminho absoluto

class MotoristViewSet(viewsets.ModelViewSet):
    queryset = MotoristModel.objects.all()
    serializer_class = MotoristSerializer