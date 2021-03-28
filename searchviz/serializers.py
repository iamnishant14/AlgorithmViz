from rest_framework import serializers

from .models import SearchName


class SearchNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchName
        fields = ('id', 'name', 'description')
