#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Name App 	: Calculo de angulos interiores
	Description	: Se calcular los angulos interiores de un polígono.
	Created 	: Heber DANIEL Ramos Mendoza (HDRamosMendoza)
	Email		: heber.daniel.ramos.mendoza@gmail.com
	Position 	: GIS Developer
	Location 	: Perú/Lima/San Juan de Lurigancho
	Social media: HDRamosMendoza
	Phone		: 999130638
	Web			: https://hdramosmendoza.github.io/Perfil-Profesional/
	Copyright	: Heber Daniel Ramos Mendoza
	Licence		: Favor de mencionar al autor
"""

import os
import os.path
import arcpy
import math
import glob
import shutil

arcpy.SpatialReference(4326)
arcpy.env.workspace = os.path.join(os.getcwd(), 'SHP')

_inPathFile = arcpy.GetParameterAsText(0);
_outPathFile = arcpy.GetParameterAsText(1);
_inFC = arcpy.GetParameterAsText(2);

"""
Ángulo central	| Área
	360°		   πr²
	 Ø			   x

- Regla de 3 simples directa: Asc X = ((Ø*πr²)/360°)
- Longitud de la circunferencia: 2πr
- Área del círculo: A = πr²
- Arco de circuferencia: Región limitado por 2 radios y un arco de circuferneia.

Ejemplo: Ø = 75° , r = 10cm , Asc = ?
Asc X = ((Ø*πr²)/360°)
Asc X = 65.4 cm²

_ab = math.pow(10,2)
_abc = (math.pi * 75 * math.pow(10,2))/360
"""

def package():
	_fileList=[]
	for path, namePath, fileNames in os.walk(arcpy.env.workspace):
		for fileName in fileNames:
			if(fileName.endwith('.shp')):
				_fileList.append(os.path.join(path, fileName))
	return _fileList
    
def removeFile(path):
	if os.path.isdir(path):
		shutil.rmtree(path)
	os.makedirs(path)
	#_files = glob.glob(path)
	
def main():
	try:
	    _pathTemp = os.path.join(os.getcwd(), 'TEMP')
	    removeFile(_pathTemp)
	    _inFC = os.path.join(arcpy.env.workspace,'Poly.shp')
	    arcpy.MakeFeatureLayer_management(_inFC, 'Poly')
	    for row in arcpy.da.SearchCursor('Poly', ["OID@", "SHAPE@"]):
	    	_partnum = 0
	    	for part in row[1]:
		        _tempName = 0
		        for pnt in part:
		            if pnt:
		                _jsonPointESRI = {"type": "Point", "coordinates": [pnt.X, pnt.Y], "spatialReference": {"wkid": 4326}}
		                _outFC_PNT = arcpy.AsShape(_jsonPointESRI)
		                _bufferFC = arcpy.Buffer_analysis(
		                    in_features 			 =_outFC_PNT,
		                    out_feature_class 		 =os.path.join(_pathTemp, 'BUFFER_{}.shp'.format(_tempName)),
		                    buffer_distance_or_field ='1 Meters',
		                    line_side 				 ='FULL',
		                    line_end_type 			 ='ROUND',
		                    dissolve_option 		 ='ALL'
		                )
		                _clipFC = arcpy.Clip_analysis('Poly', _bufferFC, os.path.join(_pathTemp, 'CLIP_{}.shp'.format(_tempName)))

		                with arcpy.da.SearchCursor(_clipFC,['SHAPE@AREA']) as cursor:
		                	for row in cursor:
		                		_angulo = ((row[0]*360)/math.pi)
		                		print('Vertex angle (X - {0}, Y - {1}): {2}'.format(pnt.X,pnt.Y,_angulo))

		            else:
		                print("Interior")

		            _tempName += 1

		        _partnum += 1
	except IOError as err:
		errorTime = time.strftime("%H:%M:%S")
		print("Error OS {0}").format(err)
		with open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'a') as f:
			f.write(str(errorTime)+ '\n')
			f.write(err.message + '\n')
			f.close()      

if __name__ == "__main__":
    main()

'''
_inFC = package()
for fileName in _inFC
	_outFile = fileName.replace(_inPathFile,_outPathFile)
	_outPackage = os.path.dirname(os.path.realpath(_outFile))
	if not os.path.exits(_outPackage):
		os.makedirs(_outPackage)
	arcpy.Clip_analysis(fileName,_inFC,_outFile)
arcpy.AddMessage("Fin del proceso")
'''