from rest_framework import serializers
from .models import Category, Tag
from django.db.models import Prefetch

class CategoryChildrenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'url', 'count_articles', 'children')


class CategoryListSerializer(serializers.ModelSerializer):
  children = CategoryChildrenSerializer(many=True)
  
  class Meta:
    model = Category
    fields = ('id', 'name', 'url', 'count_articles', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'url', 'count_articles', 'title', 'description', 'keywords', 'text',)


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'name', 'url', 'count_articles',)