'''from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import serializers
from django.urls import reverse

UserModel = get_user_model()

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            UserModel.objects.get(email=value)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def send_reset_email(self):
        user = UserModel.objects.get(email=self.validated_data['email'])
        uid = default_token_generator.make_token(user)
        token = default_token_generator.make_token(user)
        reset_password_link = reverse('reset_password', kwargs={'uidb64': uid, 'token': token})
        reset_password_link = self.context['request'].build_absolute_uri(reset_password_link)

        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_password_link}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

class ResetPasswordSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, data):
        try:
            uid = default_token_generator.check_token(data['uidb64'])
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise serializers.ValidationError("Invalid user.")
        
        if not default_token_generator.check_token(user, data['token']):
            raise serializers.ValidationError("Invalid token.")
        
        return data

    def save(self, **kwargs):
        user = UserModel.objects.get(pk=self.validated_data['uidb64'])
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ResetPasswordSerializer(serializers.Serializer):
    uidb64 = serializers.IntegerField()
    token = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, data):
        user_id = data.get('uid64')
        token = data.get('token')

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("Invalid user.")

        # Check if the token is valid for the user
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError("Invalid token.")
        
        return data

    def save(self, **kwargs):
        user_id = self.validated_data['uid64']
        user = UserModel.objects.get(pk=user_id)
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user'''

