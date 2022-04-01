from rest_framework.generics import ListAPIView

from .models import Region
from .serializers import RegionSerializer

class RegionListAPIView(ListAPIView):
  queryset = Region.objects.filter(is_active = True)
  serializer_class = RegionSerializer