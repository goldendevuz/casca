from adrf.serializers import ModelSerializer
from rest_framework import serializers

from domain.entities.models.barber import Barber, Favorite, History, SecuritySetting, WorkingHour
from domain.entities.models.barbershop import Barbershop, Specialty


class BarberSerializer(ModelSerializer):
    specialty = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(),
        required=True,
        allow_null=False
    )
    barbershop = serializers.PrimaryKeyRelatedField(
        queryset=Barbershop.objects.all(),
        required=True,
        allow_null=False
    )

    class Meta:
        model = Barber
        exclude = ['user']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ['user']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class SecuritySettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecuritySetting
        exclude = ['user']


class WorkingHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHour
        fields = '__all__'

    def validate(self, data):
        start = data.get('start_time')
        end = data.get('end_time')
        if start and end and start >= end:
            raise serializers.ValidationError("Ish boshlanish vaqti tugash vaqtidan oldin bo'lishi kerak.")
        return data
