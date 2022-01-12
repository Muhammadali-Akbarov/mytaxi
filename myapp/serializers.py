from rest_framework.serializers import ModelSerializer
from .models import Driver,Client,Order


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
    
    def create(self, validated_data):
        driver = Driver(**validated_data)
        driver.other = 1
        
        driver.save()
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()

        return instance
    
    
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    def create(self, validated_data):
        client = Client(**validated_data)
        client.other = 1
        
        client.save()
    
    def update(self, instance, validated_data):
        instance.client_name = validated_data.get("client_name")
        instance.save()

        return instance
    

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get("status")
        instance.save()

        return instance

