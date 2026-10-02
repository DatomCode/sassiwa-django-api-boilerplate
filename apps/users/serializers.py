from rest_framework import serializers
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "fullname",
            "created_at",
            "updated_at",
            "password",
        ]
        read_only_fields = ["created_at", "updated_at", "id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
