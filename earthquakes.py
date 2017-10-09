"""
USGS (US Geological Survey) publishes various earthquake data as JSON feed. Here's a feed spanning all domestic earthquages from the past week:
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson

Using this JSON feed:
1) identify every earthquake in California from past week,
2) list them chronologically (ascending),
3. and finally output in a format resembling the following e.g.:

2017-07-13T20:43:37+00:00 | 3km NW of Greenville, California | Magnitude: 1
2017-07-13T22:09:53+00:00 | 41km SW of Ferndale, California | Magnitude: 2.76
2017-07-13T22:31:04+00:00 | 11km E of Mammoth Lakes, California | Magnitude: 1.31
2017-07-13T22:32:48+00:00 | 15km SE of Mammoth Lakes, California | Magnitude: 0.92
2017-07-13T22:37:52+00:00 | 12km E of Mammoth Lakes, California | Magnitude: 0.95
2017-07-13T22:45:28+00:00 | 37km SE of Bridgeport, California | Magnitude: 1.7
2017-07-13T22:49:58+00:00 | 8km ENE of Mammoth Lakes, California | Magnitude: 0.92
2017-07-13T22:54:30+00:00 | 3km SE of Atascadero, California | Magnitude: 2.04
"""

import json
import urllib2
import re
import time
import sys
import pprint

earthquakes = json.load(urllib2.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"))


#pprint.pprint(earthquakes)

#print earthquakes['coordinates']

#for key in earthquakes.keys():
#    print 'key=%s, value=%s' % (key, earthquakes[key])
    
    
print "\n\n"
#print type(earthquakes)



#print earthquakes['features'][5]['properties']['updated']

listOfQuakesInCa = []

numQuakes = len(earthquakes['features'])

for i in range(0,numQuakes):
    title = earthquakes['features'][i]['properties']['title']
    details = title.split(",")
    state = details[-1]
    if ('California' in state) or ('CA' in state):
        epochTime = earthquakes['features'][i]['properties']['updated']
        listOfQuakesInCa.append(str(epochTime) + " - " + title)
        



listOfQuakesInCa.sort()


for quake in listOfQuakesInCa:
    components = quake.split("-")
    epochTime = components[0]
    #quakeDate = time.strftime('%Y-%m-%d %H:%M:%S+00:00', time.localtime(float(epochTime)/1000))
    quakeDate = time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.localtime(float(epochTime)/1000))
    #'%Y-%m-%dT%H:%M:%SZ'
    title = components[2]
    magnitude = components[1]
    magnitude = re.sub('[M]', 'Magnitude:', magnitude)
    print quakeDate + " | " + title + " | " + magnitude


