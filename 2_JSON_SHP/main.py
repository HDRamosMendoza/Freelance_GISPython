#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import requests
import json
import arcpy
import pandas as pd
import os
import zipfile
from datetime import datetime

arcpy.SpatialReference(4326)
arcpy.env.workspace = "SHP"

nowTime = datetime.now()
nameCSV = "ListaOllas_{2}{1}{0}_{3}{4}{5}".format(nowTime.year,nowTime.month,nowTime.day,nowTime.hour,nowTime.minute,nowTime.second)
features = []
x = requests.get('https://ollascomunes.gpvlima.com/public/listaollas', verify=False)
musica_dict = json.loads(x.text)

data =[]
for item in musica_dict:
	lon = item['longitud'].replace(",",".")
	lat = item['latitud'].replace(",",".")

	if lon.endswith('.'):
		lon = lon[:-2]

	if lat.endswith('.'):
		lat = lat[:-2]
	
	item['latitud'], item['longitud'] = map(float,(lat,lon))
	data.append({
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
                })

with open('JSON/{}.json'.format(nameCSV), "w") as f:
	json.dump(data, f)

df = pd.read_json ('JSON/{}.json'.format(nameCSV))
df.to_csv ('CSV/{}.csv'.format(nameCSV), index = None, encoding='utf-8')
 
# Set the local variables
in_Table = 'CSV/{}.csv'.format(nameCSV)
x_coords = "longitud"
y_coords = "latitud"
out_Layer = nameCSV


arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords,out_Layer)
arcpy.FeatureClassToShapefile_conversion([out_Layer],r'SHP')
zfile = zipfile.ZipFile("SHP/{}.zip",format(nameCSV), "w", zipfile.ZIP_STORED)
files = os.listdir("SHP")
for f in files:
	if f.endswith("shp") or f.endswith("dbf") or f.endswith("shx"):
		zfile.write("SHP/" + f)

for f in zfile.namelist():
	print "Added %s" %f

zfile.close()


#********************************************************************** 
# Description: 
#    Zips the contents of a folder. 
# Parameters: 
#   0 - Input folder. 
#   1 - Output zip file. It is assumed that the user added the .zip  
#       extension.   #**********************************************************************  
# Import modules and create the geoprocessor 
# import sys, zipfile, arcpy, os, traceback  
# Function for zipping files.  If keep is true, the folder, along with  
#  all its contents, will be written to the zip file.  If false, only  
#  the contents of the input folder will be written to the zip file -  
#  the input folder name will not appear in the zip file. 
# 
'''
def zipws(path, zip, keep):     
	path = os.path.normpath(path)     
	# os.walk visits every subdirectory, returning a 3-tuple     
	#  of directory name, subdirectories in it, and file names     
	#  in it.     
	#     for (dirpath, dirnames, filenames) in os.walk(path):         
	# Iterate over every file name         
	#         for file in filenames:             
	# Ignore .lock files             
	#             
		if not file.endswith('.lock'):                 
			arcpy.AddMessage("Adding %s..." % os.path.join(path, dirpath, file))
		    try:                     
		    	if keep:                         
		    		zip.write(os.path.join(dirpath, file),
		    			os.path.join(os.path.basename(path),
		    			os.path.join(dirpath, file)[len(path)+len(os.sep):]))
		    	else:                         
		    		zip.write(os.path.join(dirpath, file),
		    			os.path.join(dirpath[len(path):], file))
		    except Exception, e:
		    	arcpy.AddWarning("Error adding %s: %s" % (file, e))      
		    	return None  
		    	if __name__ == '__main__':     
		    		try:         
		    			# Get the tool parameter values         
		    			#         
		    			infolder = arcpy.GetParameterAsText(0)         
		    			outfile = arcpy.GetParameterAsText(1)                        
		    			# Create the zip file for writing compressed data. In some rare         
		    			#  instances, the ZIP_DEFLATED constant may be unavailable and         
		    			#  the ZIP_STORED constant is used instead.  When ZIP_STORED is         
		    			#  used, the zip file does not contain compressed data, resulting         
		    			#  in large zip files.          
		    			#         
		    			try:                 
		    			zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED)                 
		    			zipws(infolder, zip, True)                
		    			 zip.close()         
		    			except RuntimeError:                 
		    			# Delete zip file if it exists                 
		    			#                 
		    			if os.path.exists(outfile):                        
		    			 	os.unlink(outfile)                 
		    			 	zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_STORED)                 
		    			 	zipws(infolder, zip, True)                 
		    			 	zip.close()                 
		    			 	arcpy.AddWarning("    Unable to compress zip file contents.")                             
		    			 	arcpy.AddMessage("Zip file created successfully")      
		    			except:         
		    			 	# Return any Python specific errors as well as any errors from the geoprocessor         
		    			 	#         
		    			tb = sys.exc_info()[2]         
		    			tbinfo = traceback.format_tb(tb)[0]        
		    			pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n" 
		    			arcpy.AddError(pymsg)
		msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"         arcpy.AddError(msgs)
'''