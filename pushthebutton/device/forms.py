# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import Device


class DeviceForm(FlaskForm):
    """Device editing form."""

    short_name = StringField(u'Short name', [DataRequired(), Length(max=30)])
    information = TextAreaField(u'Information',
                    description=u'Instructions for responding to event')

    current_lat = FloatField(u'Latitude', default=48.182601)
    current_lon = FloatField(u'Longitude', default=11.304939)
    is_active = BooleanField(u'Active', default=True)

    device_api = StringField('Device API address')
    device_key = StringField('Device API key')
    device_id = StringField('Device API id')

    submit = SubmitField(u'Save')
