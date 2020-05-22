from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll, Choice
from .serializers import PollSerializer
# Create your views here.


class PollList(APIView):
	def get(self, request):
		polls = Poll.objects.all()[:20]
		data= PollSerializer(polls, many= True).data
		return Response(data)


class PollDetail(APIView):
	def get(self, request, pk):
		poll= get_object_or_404(Poll, pk=pk)
		data= PollSerializer(poll).data
		return Response(data)