from rest_framework import serializers
from .models import pereval_added


class PerevalSerializers(serializers.ModelSerializer):
    class Meta:
        model = pereval_added
        fields = ('row_data', 'images')