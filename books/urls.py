from django.urls import path, include

from main.settings import REST_FRAMEWORK

from . views import (
    index,
    Login,
    BookViewSet
)


# REST_FRAMEWORK routers
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [

    path('', index, name='index'),
    path('api/login/', Login.as_view(), name='login'),
    path('api/', include(router.urls)),
]
