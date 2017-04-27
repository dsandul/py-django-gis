from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import JSONField
from django.db import models


class Timed(models.Model):
    ins_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    upd_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Type(models.Model):
    """
    Type of Company
    """
    GYM = 'gym'
    FITNESS_CENTER = 'fitness_center'
    MEDICAL_CENTER = 'medical_center'
    BEAUTY_SALON = 'beauty_salon'
    DANCE_STUDIO = 'dance_studio'
    TYPES = (
        (GYM, 'Gym'),
        (FITNESS_CENTER, 'Fitness center'),
        (MEDICAL_CENTER, 'Medical center'),
        (BEAUTY_SALON, 'Beauty salon'),
        (DANCE_STUDIO, 'Dance studio')
    )
    name = models.CharField(choices=TYPES, max_length=128)
    description = models.CharField(max_length=1024, null=True, blank=True)


class Company(Timed, models.Model):
    """
    Company Instance
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, null=True, blank=True)
    address = models.CharField(max_length=512, null=True)
    geo_position = PointField(null=True)
    state = models.SmallIntegerField(default=0)
    type = models.ForeignKey(Type, null=True)
    website = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    is_parking = models.BooleanField(default=True)  # if parking place
    landmark = models.CharField(max_length=256, null=True)  # orient place
    main_image_url = models.CharField(max_length=512, null=True)


class City(models.Model):
    """
    List of supported Cities
    """
    name_en = models.CharField(max_length=256, default='Unnamed City')
    name_rus = models.CharField(max_length=256, null=True, blank=True)
    geo_position = PointField(null=True)
    country = models.CharField(max_length=256, null=True, blank=True)


class MetroLine(models.Model):
    """
    List of Metro lines
    """
    name_en = models.CharField(max_length=256, default='Unnamed Metro Line')
    name_rus = models.CharField(max_length=256, null=True, blank=True)
    city = models.ForeignKey(City, null=True)


class MetroStation(models.Model):
    """
    List of Metro stations
    """
    name_en = models.CharField(max_length=256, default='Unnamed Metro Station')
    name_rus = models.CharField(max_length=256, null=True, blank=True)
    line = models.ForeignKey('MetroLine', null=False)
    geo_position = PointField(null=True, blank=True)
