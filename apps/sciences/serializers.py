from rest_framework import serializers

from apps.sciences.models import Sciences


class SciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sciences
        fields = "__all__"
