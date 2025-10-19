from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snay3i.models.user import User

from snay3i.serializers.user import UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: add custom permission classes
