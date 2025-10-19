from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.task import Task

from snay3i.serializers.task import TaskSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'task': reverse('task-list', request=request, format=format),
    })

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
