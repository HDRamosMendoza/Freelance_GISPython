#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd 
#import csv
#from datetime import datetime
#from geojson import Feature, FeatureCollection, Point
'''	Requirements: pip install geojson '''

print(os.path.join(os.getcwd()))

#pd.to_excel()
#pd.to_csv()


'''
# 1. Se obtiene parte del nombre del archivo
nowTime = datetime.now()
# Día - Mes - Año - Horas - Minutos - Segundos - Milisegundos
nameCSV = "MSI_{2}{1}{0}_{3}{4}{5}".format(nowTime.year,nowTime.month,nowTime.day,nowTime.hour,nowTime.minute,nowTime.second)
# 2. Se abre el CSV para escribir
with open('CSV/{}.csv'.format(nameCSV),'w') as writerCSV:
	# 3. Se lee el CSV para escribir en el primer CSV
	with open('SOURCE/20200609184622.csv') as readerCSV:
		rowCSV = csv.DictReader(readerCSV)
		writer = csv.DictWriter(writerCSV,fieldnames=rowCSV.fieldnames)
		writer.writeheader()
		for item in rowCSV:
			item['Longitude'] = item['Longitude'].replace("West:","-")
			item['Latitude']  = item['Latitude'].replace("South:","-")
			writer.writerow(item)

features = []
with open('CSV/{}.csv'.format(nameCSV)) as csvFile:
    rowCSV = csv.DictReader(csvFile)
    for item in rowCSV:
    	latitude, longitude = map(float,(item['Latitude'], item['Longitude']))
    	features.append(
            Feature(
                geometry = Point((longitude,latitude)),
                properties = {
                    'N':item['\xef\xbb\xbfNo.'],
			    	'Device Name':item['Device Name'],
			    	'Receiving Time':item['Receiving Time'],
			    	'GPS Time':item['GPS Time'],
			    	'Speed':item['Speed'],
			    	'Direction':item['Direction'],
			    	'BaseStation ID':item['BaseStation ID'],
			    	'Channel ID':item['Channel ID']
                }
            )
        )

collection = FeatureCollection(features)
with open('CSV/{}.json'.format(nameCSV), "w") as f:
    f.write('%s' % collection)
'''