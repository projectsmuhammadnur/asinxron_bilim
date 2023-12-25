from django.urls import path

from apps.topics.views import TopicsFilterViewSet

urlpatterns = [
    path('filter/<int:science_id>/', TopicsFilterViewSet.as_view(),
         name='topics-filter')
]
