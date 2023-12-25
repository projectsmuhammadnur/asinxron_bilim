from django.shortcuts import get_list_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.topics.models import Topics
from apps.topics.serializers import TopicsSerializer


class TopicsFilterViewSet(ListAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return get_list_or_404(Topics, science_id=self.kwargs.get('science_id'))
