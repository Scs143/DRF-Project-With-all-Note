from rest_framework import serializers
from .models import DRFQuest

class DRFSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=50)
    course_name = serializers.CharField(max_length=50)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()
    
    
    def create(self, validated_data):
        return DRFQuest.objects.create(**validated_data)