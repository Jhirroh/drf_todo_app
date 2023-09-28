from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import Profile
from .serializers import ProfileSerializer, SignupSerializer, LoginSerializer


class ProfileViewSet(RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=serializer.data['username'], email=serializer.data['email'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, is_created = Token.objects.get_or_create(user=user)
        serializer = LoginSerializer(user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
