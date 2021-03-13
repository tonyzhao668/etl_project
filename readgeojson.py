# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:18:19 2021

@author: User
"""

import urllib
import geojson
from pprint import pprint

while True:

    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2012-01-01&endtime=2017-03-01&minmagnitude=4.0&maxmagnitude=9.0&minlongitude=5.95&maxlongitude=10.50&minlatitude=45.81&maxlatitude=47.81'
    uh = urllib.request.urlopen(url)
    data = uh.read()
    pprint(data)
    break