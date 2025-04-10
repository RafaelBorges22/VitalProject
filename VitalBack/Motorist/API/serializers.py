from rest_framework import serializers
from Motorist.models import MotoristModel  

class MotoristSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotoristModel
        fields = '__all__'