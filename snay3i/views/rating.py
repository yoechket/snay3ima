from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.rating import Rating

from snay3i.serializers.rating import RatingSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rating': reverse('rating-list', request=request, format=format),
    })

class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
