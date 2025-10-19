from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.intervention import Intervention

from snay3i.serializers.intervention import InterventionSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'interventions': reverse('intervention-list', request=request, format=format),
    })

class InterventionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
