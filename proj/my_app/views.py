from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from my_app.serializers import UserSerializer
from django.contrib.auth.models import User


class Profile(APIView):
    # Получаем данные пользователя
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return HttpResponse({})

    def post(self, request):
        user = User.objects.filter(username=request.data['profile']['username'])
        if user.exists() and user.first() != request.user:
            return HttpResponse(status=403)
        request.user.username = request.data['profile'].get('username', '')
        request.user.first_name = request.data['profile'].get('first_name', '')
        request.user.last_name = request.data['profile'].get('last_name', '')
        request.user.email = request.data['profile'].get('email', None)
        request.user.save()
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class Authorization(APIView):
    # Происходит авторизация пользователя
    def post(self, request):
        user = authenticate(request, username=request.data.get('login', ''), password=request.data.get('password', ''))
        if user is not None:
            login(request, user)
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return HttpResponse(status=403)


class Registration(APIView):
    def post(self, request):
        if User.objects.filter(username=request.data['login']).exists():
            return HttpResponse(status=403)
        user = User.objects.create_user(request.data['login'], password=request.data['password'])
        user.save()
        return HttpResponse(status=200)

    def delete(self, request):
        request.user.delete()
        return HttpResponse(status=200)
        user = authenticate(request, username=request.data.get('login', ''), password=request.data.get('password', ''))
        if user is not None:
            user.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)
        return JsonResponse({})


class Logout(APIView):
    def post(self, request):
        logout(request)
        return HttpResponse(status=200)


