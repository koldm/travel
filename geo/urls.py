from django.urls import path

from .views import RegionListAPIView

urlpatterns = [
    path('', RegionListAPIView.as_view(), name='list'),
]
