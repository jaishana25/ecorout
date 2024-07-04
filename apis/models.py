from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Trips(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    source_latitude = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^-?\d{1,2}\.\d{1,6}$',
                message='Enter a valid latitude with up to 6 decimal places.'
            )
        ])
    source_longitude = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^-?\d{1,2}\.\d{1,6}$',
                message='Enter a valid longitude with up to 6 decimal places.'
            )
        ])
    destination_latitude = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^-?\d{1,2}\.\d{1,6}$',
                message='Enter a valid latitude with up to 6 decimal places.'
            )
        ])
    destination_longitude = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^-?\d{1,2}\.\d{1,6}$',
                message='Enter a valid longitude with up to 6 decimal places.'
            )
        ])
    trip_date = models.DateField()
    trip_time = models.TimeField()

    def __str__(self):
        return f"Trip by {self.profile.name} on {self.trip_date}"
