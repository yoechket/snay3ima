from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.profession import Profession

from snay3i.serializers.profession import ProfessionSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'professions': reverse('profession-list', request=request, format=format),
    })


class ProfessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]  # TODO: add custom permission classes

    class Meta:
        verbose_name = "Profession"
        ordering = ['name']
        verbose_name_plural = "Professions"
