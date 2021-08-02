from django.http import HttpResponse
from django.shortcuts import render
from .serializers import AmiiboChartSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets

'''class AmiiboChartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset
    serializer_class = AmiiboChartSerializer
    filter_backends = [DjangoFilterBackend]
''' 

