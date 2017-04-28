import django_filters
from django.contrib.auth.models import User, Group
from dstechapi import models
from dstechapi import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


"""
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
"""


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    distance_filter_field = 'geo_position'
    filter_backends = (DistanceToPointFilter,)
    distance_filter_convert_meters = True
    bbox_filter_include_overlapping = True


class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class MetroLineViewSet(viewsets.ModelViewSet):
    queryset = models.MetroLine.objects.all()
    serializer_class = serializers.MetroLineSerializer


class MetroStationFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = models.MetroStation
        fields = ['line']


class MetroStationViewSet(viewsets.ModelViewSet):
    queryset = models.MetroStation.objects.all()
    serializer_class = serializers.MetroStationSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = MetroStationFilter
