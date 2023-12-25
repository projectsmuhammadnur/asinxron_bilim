from django.shortcuts import get_list_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from apps.tests.models import Tests
from apps.tests.serializers import TestsSerializer


class TestsDetailViewSet(RetrieveAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    permission_classes = [AllowAny]


class TestsFilterViewSet(ListAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return get_list_or_404(Tests, topic_id=self.kwargs.get('topic_id'))
