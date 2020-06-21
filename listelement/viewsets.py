from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Element, Category, Type
from .serializer import ElementSerializer, CategorySerializer, TypeSerializer
from rest_framework.response import Response

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    '''def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(user)
        return Response(serializer.data)'''

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer