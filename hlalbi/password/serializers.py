
from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=4)
    confirm_password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        fields = ("password", "confirm_password",)

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return data

