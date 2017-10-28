# -*- coding: utf-8 -*-
"""Devices refresh."""

from .models import Device

import requests

from flask import current_app

from ..database import db

TTN_URL = 'https://%s.data.thethingsnetwork.org/api/v2/query?last=30m'

def RefreshAll():
    counter = 0
    for dev in Device.query.filter_by(is_active=True).all():
        if not dev.device_api or not dev.device_key: continue

        url = TTN_URL % dev.device_api
        data = {
            'last': '30m'
        }
        headers = {
            'Accept': 'application/json',
            'Authorization': 'key %s' % dev.device_key
        }

        r = requests.get(url, headers=headers)
        if not '{' in r.text:
            current_app.logger.error(url + ': ' + r.text)
            continue
        jsondata = r.json()
        if not len(jsondata)>0:
            current_app.logger.error(jsondata)
            continue
        curdata = jsondata[0]
        dev.current_data = str(curdata)
        dev.current_status = 0
        if 'digital_in_3' in curdata:
            if curdata['digital_in_3']:
                dev.current_status = 2
        if 'level' in curdata:
            if curdata['level'] > 510:
                dev.current_status = 1
            if curdata['level'] > 530:
                dev.current_status = 2
        dev.device_id = curdata['device_id']
        dev.update()
        db.session.add(dev)
        counter = counter + 1
    db.session.commit()
    return counter
