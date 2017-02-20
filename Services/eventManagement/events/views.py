import requests
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(style={'input_type': 'password'})


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(request.data)
        response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                                 data=serializer.data)

        if 'token' not in response.json():
            return Response(status=status.HTTP_403_FORBIDDEN)

        token = response.json()['token']
        headers = {"Authorization": token}
        request.META.update(headers)
        request.method = 'GET'
        return EventsView.as_view()(request)


class EventsView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        token = request.META['Authorization']
        verify = requests.post('http://127.0.0.1:8000/api-token-verify/', data={'token': token})

        if verify.json()['token'] == token:
            username = verify.json()['user']['username']

        data = {
            'username': username,
            'content': 'Events Website works now :)'
        }
        return Response(data)
