from rest_framework.generics import ListAPIView
from .models import SearchName
from .serializers import SearchNameSerializer


class SearchAPI(ListAPIView):
    queryset = SearchName.objects.all()
    serializer_class = SearchNameSerializer
