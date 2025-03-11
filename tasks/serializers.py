from rest_framework import serializers

from .models import CustomUser, Task
import re 


class CustomUserSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(
        many=True, read_only=True
    )  # string reprasentation of tasks

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "password", "task"]

    def create(self, validated_data):
        password = validated_data.pop("password")  # Extract password
        user = CustomUser(**validated_data)
        user.set_password(password)  # Hash password
        user.save()
        return user

    def update(self, instance, validated_data):
        # Hash password if it's being updated
        if "password" in validated_data:
            instance.set_password(validated_data.pop("password"))

        return super().update(instance, validated_data)
    
    def validate_first_name(self, value):
        """Ensure first_name contains only alphabets"""
        if not re.match(r"^[A-Za-z]+$", value):
            raise serializers.ValidationError("First name should contain only alphabets.")
        return value

    def validate_last_name(self, value):
        """Ensure last_name contains only alphabets"""
        if not re.match(r"^[A-Za-z]+$", value):
            raise serializers.ValidationError("Last name should contain only alphabets.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.EmailField(read_only=True)  # Use email instead of ID

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {"assigned_to": {"read_only": True}}
