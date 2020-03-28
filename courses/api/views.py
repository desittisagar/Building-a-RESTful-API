from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# class SubjectListView(generics.ListAPIView):
# 	queryset = Subject.objects.all()
# 	serializer_class = SubjectSerializer

# class SubjectDetailView(generics.RetrieveAPIView):
# 	queryset = Subject.objects.all()
# 	serializer_class = SubjectSerializer


class SubjectListView(APIView):
	def get(self, request):
		items = Subject.objects.all()
		serializer = SubjectSerializer(items, many = True)
		return Response(serializer.data)


class SubjectDetailView(APIView):
	def get(self, request, pk):
		#item = Subject.objects.get_or(id = pk)
		item = get_object_or_404(Subject, id=pk)
		serializer = SubjectSerializer(item)
		return Response(serializer.data)