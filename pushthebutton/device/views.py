# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required

from .models import Device
from .forms import DeviceForm

from pushthebutton.database import db

blueprint = Blueprint('device', __name__, url_prefix='/devices', static_folder='../static')

@blueprint.route('/')
@login_required
def home():
    """List devices."""
    devices = Device.query.all()
    return render_template('devices/home.html', devices=devices)

@blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def device_new():
    device = Device()
    form = DeviceForm(obj=device, next=request.args.get('next'))
    if form.validate_on_submit():
        form.populate_obj(device)
        device.update()
        db.session.add(device)
        db.session.commit()
        cache.clear()
        flash('Device added.', 'success')
        return home()
    return render_template('devices/edit.html', form=form)

@blueprint.route('/<int:device_id>/edit', methods=['GET', 'POST'])
@login_required
def device_edit(device_id):
    device = Device.query.filter_by(id=device_id).first_or_404()
    form = DeviceForm(obj=device, next=request.args.get('next'))
    if form.validate_on_submit():
        form.populate_obj(device)
        device.update()
        db.session.add(device)
        db.session.commit()
        cache.clear()
        flash('Device updated.', 'success')
        return home()
    return render_template('devices/edit.html', form=form)
