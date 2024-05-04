
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import generics, response, status
from . import serializers

class PasswordReset(generics.GenericAPIView):
    serializer_class = serializers.EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        
        if user:
            # Generate token and reset URL
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse("reset-password", kwargs={"encoded_pk": encoded_pk, "token": token})
            reset_url = f"localhost:8000{reset_url}"

            # Send reset email
            send_mail(
                'Password Reset',
                f'Click the link below to reset your password: {reset_url}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            return response.Response(
                {"message": f"Password reset link sent to {email}"},
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

class ResetPassword(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"kwargs": kwargs})
        serializer.is_valid(raise_exception=True)
        
        # Reset password
        encoded_pk = kwargs.get("encoded_pk")
        token = kwargs.get("token")
        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        user.set_password(serializer.validated_data["password"])
        user.save()

        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
