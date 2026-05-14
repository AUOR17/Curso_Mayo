from rest_framework import serializers
from .models import Gremio, Aventurero

class AventureroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aventurero
        fields = '__all__'

class GremioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gremio
        fields = '__all__'