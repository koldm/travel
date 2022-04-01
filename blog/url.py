from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView

urlpatterns = [
  path('categories/', CategoryListAPIView.as_view(), name='blog-category-list'),
  path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='blog-category-detail'),
]