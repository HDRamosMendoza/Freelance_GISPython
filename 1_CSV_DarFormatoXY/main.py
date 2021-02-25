#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
from datetime import datetime
from geojson import Feature, FeatureCollection, Point
''' 
	Requirements:
		- pip install geojson
'''
# 1. Se obtiene parte del nombre del archivo
nowTime = datetime.now()
# Día - Mes - Año - Horas - Minutos - Segundos - Milisegundos
nameCSV = "MSI_{2}{1}{0}_{3}{4}{5}".format(nowTime.year,nowTime.month,nowTime.day,nowTime.hour,nowTime.minute,nowTime.second)
# 2. Se abre el CSV para escribir
with open('CSV/{}.csv'.format(nameCSV),'w') as writerCSV:
	# 3. Se lee el CSV para escribir en el primer CSV
	with open('SOURCE/listaollas.csv') as readerCSV:
		rowCSV = csv.DictReader(readerCSV)
		writer = csv.DictWriter(writerCSV,fieldnames=rowCSV.fieldnames)
		writer.writeheader()
		
		for item in rowCSV:
			#item['Longitude'] = item['Longitude'].replace("West:","-")
			#item['Latitude']  = item['Latitude'].replace("South:","-")
			item['longitud'] = item['longitud'].replace(",",".")
			item['latitud']  = item['latitud'].replace(",",".")
			writer.writerow(item)
		

features = []
with codecs.open('CSV/{}.csv'.format(nameCSV),encoding='utf-8',errors='ignore') as csvFile:
    rowCSV = csv.DictReader(csvFile)
    for item in rowCSV:
    	print(item['latitud'])
    	print(item['longitud'])
    	latitude, longitude = map(float,(item['latitud'], item['longitud']))
    	features.append(
            Feature(
                geometry = Point((longitude,latitude)),
                properties = {
                    'id': item['id'],
			    	'correo': item['correo'],
			    	'distrito': item['distrito'],
			    	'zona': item['zona'],
			    	'aahh': item['aahh'],
			    	'ubicacion': item['ubicacion'],
			    	'agua': item['agua'],
			    	'luz': item['luz'],
			    	'nombre_olla': item['nombre_olla'],
			    	'nombre_contacto': item['nombre_contacto'],
			    	'cargo_contacto': item['cargo_contacto'],
			    	'celular_contacto': item['celular_contacto'],
			    	'presencia_muni': item['presencia_muni'],
			    	'insumos': item['insumos'],
			    	'org_ayuda': item['org_ayuda'],
			    	'instrumentos': item['instrumentos'],
			    	'dias_atencion': item['dias_atencion'],
			    	'comidas_dia': item['comidas_dia'],
			    	'raciones': item['raciones'],
			    	'precio_racion': item['precio_racion'],
			    	'raciones_pagadas': item['raciones_pagadas'],
			    	'zonas_beneficiadas': item['zonas_beneficiadas'],
			    	'familias_beneficiadas': item['familias_beneficiadas'],
			    	'ninos_beneficiadas': item['ninos_beneficiadas'],
			    	'adultos_beneficiadas': item['adultos_beneficiadas'],
			    	'disca_beneficiadas': item['disca_beneficiadas'],
			    	'emba_beneficiadas': item['emba_beneficiadas'],
			    	'enfercro_beneficiadas':item['enfercro_beneficiadas'],
			    	'observaciones': item['observaciones'],
			    	'total_beneficiadas': item['total_beneficiadas'],
			    	'foto':item['foto'],
			    	'latitud':item['latitud'],
			    	'longitud':item['longitud'],
			    	'estado':item['estado'],
			    	'padrones':item['padrones'],
			    	'comedorpopular':item['comedorpopular'],
			    	'comite':item['comite'],
			    	'nombre_contacto_secundario':item['nombre_contacto_secundario'],
			    	'cargo_contacto_secundario':item['cargo_contacto_secundario'],
			    	'celular_contacto_secundario':item['celular_contacto_secundario'],
			    	'tipo_espacio':item['tipo_espacio'],
			    	'estado_espacio':item['estado_espacio'],
			    	'combustible':item['combustible'],
			    	'techo':item['techo'],
			    	'lavado':item['lavado'],
			    	'higiene':item['higiene'],
			    	'huerto':item['huerto'],
			    	'espacio_huerto':item['espacio_huerto'],
			    	'liderazgo':item['liderazgo'],
			    	'inocuidad':item['inocuidad'],
			    	'protocolos':item['protocolos'],
			    	'extranjera':item['extranjera'],
			    	'otro_cap':item['otro_cap'],
			    	'created_at':item['created_at'],
			    	'updated_at':item['updated_at']
                }
            )
        )

collection = FeatureCollection(features)
with open('CSV/{}.json'.format(nameCSV), "w") as f:
    f.write('%s' % collection)