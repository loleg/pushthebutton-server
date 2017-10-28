# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from pushthebutton.database import Column, Model, SurrogatePK, db, reference_col, relationship
from pushthebutton.extensions import bcrypt


class Device(SurrogatePK, Model):
    """A device in the field."""

    __tablename__ = 'devices'
    short_name = Column(db.String(30), unique=True, nullable=False)
    information = Column(db.UnicodeText(), nullable=True, default=u"")

    current_lat = Column(db.Float(), nullable=True)
    current_lon = Column(db.Float(), nullable=True)
    current_data = Column(db.UnicodeText(), nullable=True, default=u"")
    current_status = Column(db.Integer(), nullable=True, default=0)

    device_api = Column(db.String(100), nullable=True)
    device_key = Column(db.String(80), nullable=True)
    device_id = Column(db.String(80), nullable=True)

    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    is_active = Column(db.Boolean(), default=False)

    # User owner
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='projects')

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Device({name!r})>'.format(name=self.short_name)
