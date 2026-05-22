from rest_framework import serializers
from . models import table

class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = table
        fields = '__all__'
