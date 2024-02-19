from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Page
from blog.serializers import PageSerializer


class PageModelViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
