import json
import math
import requests
with open('side_walk_new.json') as data_file:
    sidewalk = json.load(data_file)

sidewalkWithElevation = []
count = 0
while(count<=14100):
    for i in sidewalk:
        for j in i['coordinates']:
            lng = j[0]
            lat = j[1]
            lnglat = (j[1],j[0])
            lng = str(j[0])
            lat = str(j[1])
            #data = requests.get("https://open.mapquestapi.com/elevation/v1/profile?key=GvSYS7L1XFRSN12CJU1oPtBbNjayDgVJ&shapeFormat=raw&latLngCollection="+lat","+lng)
            data = requests.get("https://open.mapquestapi.com/elevation/v1/profile?key=GvSYS7L1XFRSN12CJU1oPtBbNjayDgVJ&shapeFormat=raw&latLngCollection="+lat+","+lng)
            data = data.json()
            elevation = data["elevationProfile"][0]['height']
            lnglatWithElevation = (lnglat,elevation)
            sidewalkWithElevation.append(lnglatWithElevation)
            count += 1
            if (count == 14000):
                with open('dataWithElevation.json', 'w') as outfile:
                    json.dump(sidewalkWithElevation, outfile)
