from rest_framework.generics import ListAPIView

from apps.sciences.models import Sciences
from apps.sciences.serializers import SciencesSerializer


class SciencesListViewSet(ListAPIView):
    queryset = Sciences.objects.all()
    serializer_class = SciencesSerializer
