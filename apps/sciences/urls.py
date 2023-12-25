from django.urls import path

from apps.sciences.views import SciencesListViewSet

urlpatterns = [
    path('', SciencesListViewSet.as_view(),
         name='sciences-list')
]
