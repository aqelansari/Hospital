from rest_framework import serializers
from .models import Counsellor
from django.contrib.auth.hashers import make_password
import re


class CounsellorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Counsellor
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if not re.findall('[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        
        if not re.findall('[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        
        if not re.findall('[0-9]', value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        
        if not re.findall('[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return value

    def create(self, validated_data):
        validated_data['is_active'] = True
        counsellor = Counsellor.objects.create(**validated_data)
        return counsellor
    
    def update(self, instance, validated_data):
        # Handle updates, ensuring password is hashed on update operations too
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'])
        instance.save()
        return instance