from adrf import serializers
from domain.entities.models.barbershop import Barbershop, Specialty, Service, Banner, ContactUs

class BarbershopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbershop
        fields = '__all__'

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
