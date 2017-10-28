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
    return render_template('devices/map.html')

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
    return render_template('devices/new.html', form=form)
