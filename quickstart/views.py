from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
'''
Function Based Api View

'''
# @csrf_exempt //api view use na korle ata use korte hbe

# @api_view(['GET', 'POST'])
# def article_list(request):
# 	if request.method== 'GET':
# 		articles = Article.objects.all()
# 		serializer= ArticleSerializer(articles, many=True)
# 		return Response(serializer.data)

# 	elif request.method== 'POST':
# 		#data = JSONParser().parse(request) #api view use na korle ata use korte hbe
# 		serializer= ArticleSerializer(data= request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

# # @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):
# 	try:
# 		article= Article.objects.get(pk=pk)
	
# 	except:
# 		return Response(status=status.HTTP_404_NOT_FOUND)


# 	if request.method =='GET':
# 		serializer= ArticleSerializer(article)
# 		return Response(serializer.data)
# 	if request.method== 'PUT':
# 		# data= JSONParser.parse(request)
# 		serializer=  ArticleSerializer(article, data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

# 	if request.method=='DELETE':
# 		article.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


'''
Class Based APIView

'''

# class ArticleView(APIView):
	
# 	def get(self, request):
# 		articles = Article.objects.all()
# 		serializer= ArticleSerializer(articles, many=True)
# 		return Response(serializer.data)

# 	def post(self, request):
# 		serializer= ArticleSerializer(data= request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

# class ArticleDetail(APIView):
# 	def get_object(self,id):
# 		try:
# 			article= Article.objects.get(id=id)
# 			return(article)
# 		except:
# 			return Response(status=status.HTTP_404_NOT_FOUND)

# 	def get(self, request, id):
# 		article= self.get_object(id)
# 		serializer = ArticleSerializer(article)
# 		return Response(serializer.data)

# 	def put(self,request,id):
# 		article= self.get_object(id)
# 		serializer=  ArticleSerializer(article, data=request.data)
# 		if serializer.is_valid():
#  			serializer.save()
#  			return Response(serializer.data)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

# 	def delete(self,request,id):
# 		article=self.get_object(id)
# 		article.delete()
# 		return Response(status=status.HTTP_404_NOT_FOUND)


'''
    Generic API Views /concrit

'''

# class GenericAPIView(generics.ListCreateAPIView):
# 	serializer_class = ArticleSerializer
# 	queryset = Article.objects.all()
# 	#authentication_classes = [SessionAuthentication, BasicAuthentication]
# 	authentication_classes=[TokenAuthentication]
# 	permission_classes=[IsAuthenticated]

# # class GenericDetailAPIView(generics.RetrieveDestroyAPIView, mixins.UpdateModelMixin):
# # 	serializer_class=ArticleSerializer
# # 	queryset = Article.objects.all()	
# # 	def put(self, request, pk=None):
# # 		return self.update(request,pk)


# class GenericDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
# 	serializer_class=ArticleSerializer
# 	queryset = Article.objects.all()	
	
'''
Class View Set
'''


# class ArticleViewSet(viewsets.ViewSet):

# 	def list(self, request):
# 		articles= Article.objects.all() 
# 		serializer = ArticleSerializer(articles, many=True)
# 		return Response(serializer.data)


# 	def create(self, request):
# 		serializer= ArticleSerializer(data= request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


# 	def retrieve(self, request, pk):
# 		queryset = Article.objects.all()
# 		article = get_object_or_404(queryset,pk=pk)
# 		serializer = ArticleSerializer(article)
# 		return Response(serializer.data)

# 	def update(self, request, pk):
# 		queryset = Article.objects.all()
# 		article = get_object_or_404(queryset,pk=pk)
# 		serializer=  ArticleSerializer(article, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


# 	def destroy(self, request, pk):
# 		queryset = Article.objects.all()
# 		article = get_object_or_404(queryset,pk=pk)
# 		article.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleViewSet(viewsets.GenericViewSet,generics.RetrieveUpdateDestroyAPIView,generics.ListAPIView):
	serializer_class= ArticleSerializer
	queryset = Article.objects.all()
	permission_classes=[IsAuthenticated]
	authentication_classes=[TokenAuthentication]


