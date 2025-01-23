from django.shortcuts import render
from myApp.models import *
from django.http import JsonResponse
from django.views.generic import View
import json

# Create your views here.

class SignUpView(View):
	def post(self, request, *args, **kwargs):

		try:
			data = json.loads(request.body)
			username = data['username']
			email = data['email']
			password = data['password']

			if User.objects.filter(username=username).exists():
				return JsonResponse({'error':'Username already exists'}, status=400)

			if User.objects.filter(email=email).exists():
				return JsonResponse({'error':'Email already exists'}, status=400)

			User.objects.create(username=username, email=email, password=password)
			return JsonResponse({'message':'User created successfully'}, status=201)

		except KeyError:
			return JsonResponse({'message':'missing required fields'}, status=400)

class SignInView(View):
	def post(self, request, *args, **kwargs):
		try:
			data = json.loads(request.body)
			username = data['username']
			password = data['password']

			user = User.objects.filter(username=username, password=password).first()

			if user:
				return JsonResponse({'message':'Sign In successful'}, status=200)
			else:
				return JsonResponse({'error':'Invalid credentials'}, status=401)

		except KeyError:
			return JsonResponse({'error':'Missing required fields'}, status=400)

class UserProfileView(View):
	def get(self, request, *args, **kwargs):
		try:
			username = request.GET.get('username')

			user = User.objects.filter(username=username).first()

			if user:
				user_data = {
				'username': user.username,
				'email': user.email
				}
				return JsonResponse({'user':user_data}, status=200)
			else:
				return JsonResponse({'error':'User not found'}, status=404)

		except Exception as e:
			return JsonResponse({'error':str(e)}, status=500)

class StatusView(View):
	def get(self, request, *args, **kwargs):
		return JsonResponse({'message':'alive'}, status=200)