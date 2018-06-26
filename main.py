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
from __future__ import print_function

from getTemperatureCWF import getTemperatureCyprusWeatherForecast
import os

geoJSON = 'cyprus_temperatures.geojson'
d = getTemperatureCyprusWeatherForecast(geoJSON)
d.main()

current_path = os.getcwd()
pathfile = current_path + '\\' + geoJSON
# qgis python console
print("#QGIS python console:")
print("geoJSON = '{}'".format(geoJSON))
print("current_path = '{}'".format(current_path))
print("pathfile = '{}'".format(pathfile))
print('cyprus_layer = iface.addVectorLayer(current_path + "\\\shp_qmls\\\\" + "Cyprus.shp", "Cyprus", "ogr")'.format())
print('cyprus_layer.loadNamedStyle(current_path + "\\shp_qmls\\Cyprus.qml")'.format())
print('temp_layer = iface.addVectorLayer(pathfile, geoJSON, "ogr")'.format())
print('temp_layer.loadNamedStyle(current_path + "\\\shp_qmls\\\\temp.qml")'.format())

