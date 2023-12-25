from django.urls import path, include

urlpatterns = [
    path('telegram-users/', include('apps.telegram_users.urls')),
    path('sciences/', include('apps.sciences.urls')),
    path('topics/', include('apps.topics.urls')),
    path('tests/', include('apps.tests.urls'))
]
