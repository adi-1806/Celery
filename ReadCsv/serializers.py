from rest_framework import serializers
from ReadCsv.models import StudentData
from django.core.validators import FileExtensionValidator

class CsvDataSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=True,
                                 validators=[FileExtensionValidator( ['csv'] ) ])
    owner = serializers.CharField()
    def create(self, validated_data):
        return StudentData.objects.create(**validated_data)