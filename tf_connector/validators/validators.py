from django.core.exceptions import ValidationError
import datetime


def _validate_datetime(date_time_value):
    if date_time_value < datetime.datetime.today():
        raise ValidationError()
