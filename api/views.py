from django.shortcuts import render
from polls.models import Poll, Choice
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PollSerializer, ChoiceSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        new_user = User.objects.create(username=request.data['username'], email=request.data['email'])
        serializer = UserSerializer(new_user, many=False, context={'request' : request})
        return Response(serializer.data)

class PollsViewSet(viewsets.ModelViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def create(self, request, *args, **kwargs):
        new_poll = Poll.objects.create(question=request.data['question'])
        serializer = PollSerializer(new_poll, many=False, context={'request':request})
        return Response(serializer.data)



class ChoiceViewSet(viewsets.ModelViewSet):

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer