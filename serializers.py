from django.contrib.auth.models import User, Group
from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from dstechapi import models


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
        A serializer utility class to allow us to specify the `fields` that are needed for this serializer instance
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', [])

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'url',
            'name'
        )


class TypeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only=True)

    class Meta:
        model = models.Type
        fields = (
            'id',
            'name',
            'type',
            'description'
        )


class CompanySerializer(gis_serializers.GeoFeatureModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = models.Company
        geo_field = 'geo_position'
        fields = (
            'id',
            'name',
            'address',
            'description',
            'geo_position',
            'state',
            'type_name',
            'ins_date',
            'upd_date',
            'website',
            'phone',
            'is_parking',
            'landmark'
        )


class CitySerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.City
        geo_field = 'geo_position'
        fields = (
            'id',
            'name_en',
            'name_rus',
            'geo_position',
            'country'
        )


class MetroStationSerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.MetroStation
        geo_field = 'geo_position'
        fields = (
            'id',
            'name_en',
            'name_rus',
            'line',
            'geo_position'
        )


class MetroLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetroLine
        fields = (
            'id',
            'name_en',
            'name_rus',
            'city'
        )
