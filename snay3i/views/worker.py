from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.worker import Worker

from snay3i.serializers.worker import WorkerSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'worker': reverse('worker-list', request=request, format=format),
    })

class WorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
