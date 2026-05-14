from rest_framework import viewsets
from .models import Gremio, Aventurero
from .serializers import GremioSerializer, AventureroSerializer

class GremioViewSet(viewsets.ModelViewSet):
    queryset = Gremio.objects.all()
    serializer_class = GremioSerializer

class AventureroViewSet(viewsets.ModelViewSet):
    queryset = Aventurero.objects.all()
    serializer_class = AventureroSerializer
