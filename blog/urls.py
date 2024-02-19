from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PageModelViewSet

router = DefaultRouter()
router.register(r'page', PageModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]