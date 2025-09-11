from rest_framework import serializers
from apps.v1.shared.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "langitude",
            "lattitude",
            "text",
            "name",
            "created",
            "modified",
        ]
