from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import UserSerializer, MyTokenObtainPairSerializer
from user.models import User

from .permission import ProrabPermission, MasterPermission, AdminPermission
from user.models import UserRoleChoice


# for user register
class RegiserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# for user login and creta token 
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# for auth refresh token create  
class RefreshTokenView(TokenRefreshView):
    serializer_class = MyTokenObtainPairSerializer

class UserEditView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self, request):
        return User.objects.filter(id=self.request.user.id)

class UserView(generics.ListAPIView):
    permission_classes = [AdminPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)