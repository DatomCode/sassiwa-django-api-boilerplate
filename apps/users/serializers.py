from rest_framework import serializers
from apps.users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'fullname', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**self.validated_data)