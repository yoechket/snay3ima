from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.city import City

from snay3i.serializers.city import CitySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cities': reverse('city-list', request=request, format=format),
    })

class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
