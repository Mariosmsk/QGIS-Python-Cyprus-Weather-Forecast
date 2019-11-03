# !/usr/bin/python
"""
/***************************************************************************
Name                 : Get Temperature From Cyprus Weather Forecast
Description          : Get Temperature From Cyprus Weather Forecast
Date                 : 26/June/2018
copyright            : (C) 2018 by Marios S. Kyriakou, University of Cyprus,
                       KIOS Research and Innovation Center of Excellence (KIOS CoE)
email                : mariosmsk@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import urllib3
from xml.dom import minidom
import json
import io

class getTemperatureCyprusWeatherForecast(object):

    def __init__(self, geo_jsonfile_name):
        self.geofile = open(geo_jsonfile_name, 'w')
        url = 'http://weather.cyi.ac.cy/data/met/CyDoM.xml'  # define XML location
        http = urllib3.PoolManager()
        data = http.request('GET', url)
        f = io.open('tmp.xml', 'w')
        da = data.data.decode('UTF-8')
        f.write(da)
        f.close()

        doc = minidom.parseString(da)
        self.getStations = doc.documentElement.getElementsByTagName("station")
        self.observations = doc.documentElement.getElementsByTagName("observations")

    # same size for stations and observations
    def get_data(self):
        json_data = list()
        for i, station in enumerate(self.getStations):
            for j, findTemp in enumerate(self.observations[i].getElementsByTagName("observation")):
                if findTemp.getElementsByTagName("observation_name")[0].firstChild.data == 'Temperature':
                    station_code = station.getElementsByTagName("station_code")[0].firstChild.data
                    station_lat = station.getElementsByTagName("station_latitude")[0].firstChild.data
                    station_lon = station.getElementsByTagName("station_longitude")[0].firstChild.data
                    station_date_time = self.observations[i].getElementsByTagName("date_time")[0].firstChild.data
                    station_temperature = self.observations[i].getElementsByTagName("observation")[j].getElementsByTagName("observation_value")[0].firstChild.data

                    json_data.append({"properties": {"Station": station_code, "Lat": station_lat, "Date": station_date_time.split(' ')[0],
                                       "Lon": station_lon, "Time": station_date_time.split(' ')[1], "Celsius": str(int(round(float(station_temperature)))),}, "type": "Feature",
                                      "geometry":{ "coordinates":[float(station_lon), float(station_lat)], "type": "Point"}})
        return json_data

    def main(self):
        geojson = {"type": "FeatureCollection", "crs": { "type": "name", "properties": { "name": "crs:OGC:1.3:CRS84" } },
            "features": self.get_data()}
        json.dump(geojson, self.geofile)
        self.geofile.close()