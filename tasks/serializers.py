from rest_framework import serializers

from .models import CustomUser, Task


class CustomUserSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(
        many=True, read_only=True
    )  # string reprasentation of tasks

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "task"]

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


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.EmailField(read_only=True)  # Use email instead of ID

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {"assigned_to": {"read_only": True}}

    def create(self, validated_data):
        request = self.context.get("request")  # Get request from context
        if not request or not request.user:
            raise serializers.ValidationError("User must be authenticated.")

        validated_data["assigned_to"] = request.user  # Assign the authenticated user
        return Task.objects.create(**validated_data)
