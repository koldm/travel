from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('email', 'password', 'is_guide', 'is_travel_company',)
    extra_kwargs = {
      'password': {'write_only': True},
      'is_guide': {'write_only': True},
      'is_travel_company': {'write_only': True}
    }
  
  def create(self, validated_data):
    return User.objects.create_user(**validated_data)