from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q

from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryListAPIView(ListAPIView):
  queryset = Category.objects.filter(is_active=True)
  # queryset = Category.objects.filter(Q(parent=None, depth=1) | Q(parent__is_active__exact=True, parent__depth__exact=2), is_active=True)
  serializer_class = CategoryListSerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
  queryset = Category.objects.filter(is_active=True)
  serializer_class = CategoryDetailSerializer
  

