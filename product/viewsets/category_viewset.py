# from rest_framework import status
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()