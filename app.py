#!/usr/bin/env python
from datetime import datetime
from json import loads
from requests import get

timezone = input("Fuseau Horaire : ")
rep = get('https://worldtimeapi.org/api/timezone/' + timezone)
if rep.status_code != 200 :
    raise ValueError('Erreur fuseau')
rep_json = loads(rep.text)
print(datetime.fromtimestamp(rep_json['unixtime'] + rep_json['raw_offset']))
