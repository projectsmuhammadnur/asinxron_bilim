from django.urls import path

from apps.tests.views import TestsDetailViewSet, TestsFilterViewSet

urlpatterns = [
    path('detail/<int:pk>/', TestsDetailViewSet.as_view(),
         name='tests-detail'),
    path('filter/<int:topic_id>/', TestsFilterViewSet.as_view(),
         name='tests-filter')
]
