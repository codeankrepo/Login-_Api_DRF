from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken .models import Token
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
import pyotp
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            otp = get_random_string(length=6, allowed_chars='0123456789')
            user.otp = otp
            user.save()

            send_mail(
                subject='otp verification',
                message=f'your otp: {otp}',
                from_email='app@example.com',
                recipient_list=[user.email],
                # fail_silently=False
                )
            
            return Response({'message':'user registered successfully. OTP sent for verification!'}, {f'your otp is {otp}'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        otp = request.data.get('otp')

        try:
            user = User.objects.get(mobile=mobile, otp=otp)
            user.otp = None
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message':'otp verified successfully.', 'token':token.key})
        except User.DoesNotExist:
            return Response({'message':'Invaid Mobile number or OTP'}, status=400)
        
class LogoutView(APIView):
    def post(self, request):
        request.user.auth.token.delete()
        return Response({'message':'user logged out successfully.'})