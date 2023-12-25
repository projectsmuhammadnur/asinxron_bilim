from rest_framework import serializers

from apps.tests.models import Tests


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = "__all__"
