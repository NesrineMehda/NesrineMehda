'''from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ForgotPasswordSerializer, ResetPasswordSerializer

class ForgotPasswordAPIView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_reset_email()
        return Response({'message': 'Password reset email has been sent'}, status=status.HTTP_200_OK)

class ResetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data={'uidb64': uidb64, 'token': token, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)'''







   