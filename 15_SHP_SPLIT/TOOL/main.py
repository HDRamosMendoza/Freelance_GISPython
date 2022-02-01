#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import arcpy 
arcpy.CheckOutExtension('defense')
arcpy.SpatialReference(4326)
arcpy.env.overwriteOutput = 1

nameGDB  	= 'TEMP.gdb'

pathGDBManzanas = os.path.join(os.getcwd(), '../DATA/MANZANAS.gdb')
pathTemp  	= os.path.join(os.getcwd(), '../TEMP')
pathGDBTemp = os.path.join(pathTemp, nameGDB) 

arcpy.env.workspace = pathGDBManzanas
arcpy.env.scratchWorkspace = pathGDBManzanas

def main():
	try:
		_arrFC = [] 

		if arcpy.Exists(pathGDBTemp):
   			arcpy.Delete_management(pathGDBTemp)

   		arcpy.CreateFileGDB_management(pathTemp, nameGDB)

   		_inDRENAJE = os.path.join(arcpy.env.workspace,'ADREN_BRENA_EXT')
   		_inMANZANA  = os.path.join(arcpy.env.workspace,'MZA_INEI_POB_C2017')

   		arcpy.MakeFeatureLayer_management(_inDRENAJE, 'TEMP_DRENAJE')
   		arcpy.MakeFeatureLayer_management(_inMANZANA,  'TEMP_MANZANA') 

   		arcpy.Split_analysis('TEMP_MANZANA', 'TEMP_DRENAJE', 'N_COD_GYZ', pathGDBTemp)

		arcpy.env.workspace = pathGDBTemp

		datasets = arcpy.ListDatasets(feature_type='feature')
		datasets = [''] + datasets if datasets is not None else []

		# Create FIELD MANAGEMENT
		for ds in datasets:
		    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
		        path = os.path.join(arcpy.env.workspace, ds, fc)
		        print(arcpy.Describe(path).name)
		        arcpy.AddField_management(path, "MANZANA", "TEXT", "", "", 10)
		        _arrFC.append(path)

		# Update FIELD MANZANA with name FEATURE CLASS
		fields = ['MANZANA'] 
		for ds in datasets:
			for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
				path = os.path.join(arcpy.env.workspace, ds, fc)
				with arcpy.da.UpdateCursor(path, fields) as cursor:
				    for row in cursor:
				    	row[0] = arcpy.Describe(path).name
        				cursor.updateRow(row)

   		arcpy.Merge_management(_arrFC, "MANZANAS_MERGE") 

   		for fc in _arrFC:
   			arcpy.Delete_management(fc)
   		
	except IOError as err:
		print("Error OS")


if __name__ == "__main__":
    main()