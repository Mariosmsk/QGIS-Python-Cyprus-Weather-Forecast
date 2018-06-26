# QGIS-Python-Cyprus-Weather-Forecast
Get weather data from Cyprus Weather Forecast and create a geojson file.


#QGIS python console:
geoJSON = 'cyprus_temperatures.geojson'
current_path = 'C:\Users\mkiria01\Desktop\QGIS-Python-Scripts\get Weather Cyprus Data'
pathfile = 'C:\Users\mkiria01\Desktop\QGIS-Python-Scripts\get Weather Cyprus Data\cyprus_temperatures.geojson'
cyprus_layer = iface.addVectorLayer(current_path + "\\shp_qmls\\" + "Cyprus.shp", "Cyprus", "ogr")
cyprus_layer.loadNamedStyle(current_path + "\shp_qmls\Cyprus.qml")
temp_layer = iface.addVectorLayer(pathfile, geoJSON, "ogr")
temp_layer.loadNamedStyle(current_path + "\\shp_qmls\\temp.qml")
