from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def user_registration(request):
    print("request"*88, request)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        referral_code = request.data.get('referral_code')
        if referral_code:
            referred_by = User.objects.filter(referral_code=referral_code).first()
            if referred_by:
                # Logic to award points to the user who referred this user
                pass
        user = serializer.save()
        password = request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
        token = Token.objects.create(user=user)
        return Response({'id': serializer.data['id'], 'message': 'User registered successfully', 'token': token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = User.objects.filter(referral_code=user.referral_code)
    serializer = UserSerializer(referrals, many=True)
    return Response(serializer.data)
