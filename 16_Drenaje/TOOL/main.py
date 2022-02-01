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

   		_inDRENAJE = os.path.join(arcpy.env.workspace, 'GPO_Drenaje')
   		_inMANZANA = os.path.join(arcpy.env.workspace, 'GPO_Manzana')

   		arcpy.MakeFeatureLayer_management(_inDRENAJE, 'TEMP_DRENAJE')
   		arcpy.MakeFeatureLayer_management(_inMANZANA, 'TEMP_MANZANA')

   		_pathDrenajeLine = os.path.join(pathGDBTemp, 'TEMP_DRENAJE_LINE')
   		_pathManzanaLine = os.path.join(pathGDBTemp, 'TEMP_MANZANA_LINE')

   		arcpy.PolygonToLine_management('TEMP_DRENAJE', _pathDrenajeLine) 
   		arcpy.PolygonToLine_management('TEMP_MANZANA', _pathManzanaLine) 

   		_pathDrenajeLineClip = os.path.join(pathGDBTemp, 'TEMP_DRENAJE_LINE_CLIP')
   		arcpy.Clip_analysis(
   			_pathDrenajeLine,
   			'TEMP_MANZANA',
   			_pathDrenajeLineClip
   		)

   		# Manzana LINE
   		_pathManzanaLineMerge = os.path.join(pathGDBTemp, 'TEMP_MANZANA_LINE_MERGE')
   		arcpy.Merge_management(
   			[_pathManzanaLine, _pathDrenajeLineClip],
   			_pathManzanaLineMerge
   		)

		# Manzana POLYGON
		_pathManzanaPolygon = os.path.join(pathGDBTemp, 'TEMP_MANZANA_POLYGON')
   		arcpy.FeatureToPolygon_management(
   			_pathManzanaLineMerge,
   			_pathManzanaPolygon
   		)

   		# Manzana POLYGON ALL 
		_pathManzanaPolygonUnion = os.path.join(pathGDBTemp, 'TEMP_MANZANA_POLYGON_UNION')
   		arcpy.Union_analysis(
   			in_features 		= [_pathManzanaPolygon, 'TEMP_MANZANA'],
   			out_feature_class 	= _pathManzanaPolygonUnion,
   			join_attributes 	= "ALL",
   			cluster_tolerance	= "",
   			gaps 				= "GAPS"
   		)

   		_pathManzanaUnion = os.path.join(pathGDBTemp, 'TEMP_MANZANA_UNION')
   		arcpy.Union_analysis(
   			in_features 		= ['TEMP_DRENAJE', _pathManzanaPolygonUnion],
   			out_feature_class 	= _pathManzanaUnion,
   			join_attributes 	= "ALL",
   			cluster_tolerance	= "",
   			gaps 				= "GAPS"
   		)

   		_pathManzanaAll = os.path.join(pathGDBTemp, 'TEMP_MANZANA_ALL')
		arcpy.Clip_analysis(
			in_features 		= _pathManzanaUnion,
			clip_features 		= _pathManzanaPolygonUnion,
			out_feature_class 	= _pathManzanaAll,
			cluster_tolerance	= ""
		)

		arcpy.AddField_management(_pathManzanaAll, "AREA_GRAFH", "DOUBLE", 9, "", "", "AREA_GRAFH", "NULLABLE", "NON_REQUIRED")
		arcpy.CalculateField_management(_pathManzanaAll,"AREA_GRAFH","!shape.area@squaremeters!","PYTHON_9.3","#")

		_expression = "getPoblacion(!AREA_GRAFH!,!AREA_GRAFP!,!POR_POB_C2!)"
		_codeblock = """
			def getPoblacion(GRAFH,GRAFP, C2):
        		return ((GRAFH/GRAFP) * C2)
        	"""
		arcpy.AddField_management(_pathManzanaAll, "POBLACION_HIJO", "DOUBLE", 9, "", "", "POBLACION_HIJO", "NULLABLE", "NON_REQUIRED")
		arcpy.CalculateField_management(_pathManzanaAll, "POBLACION_HIJO", _expression, "PYTHON_9.3", _codeblock)

   		arcpy.DeleteField_management(
   			_pathManzanaAll,
   			[
   				"FID_TEMP_MANZANA_POLYGON_UNION",
   				"FID_TEMP_MANZANA_POLYGON",
   				"FID_GPO_Manzana",
   				"DISTRITO",
   				"COD_GYZ",
   				"FID_GPO_Drenaje",
   				"FID",
   				"ID_MZA",
   				"Nº",
   				"NOMB_DPTO",
   				"NOMB_PROV",
   				"NOMB_DIST"
   			]
   		)

   		_arrFC.append(_pathDrenajeLine)
   		_arrFC.append(_pathManzanaLine)
   		_arrFC.append(_pathDrenajeLineClip)
   		_arrFC.append(_pathManzanaLineMerge)
   		_arrFC.append(_pathManzanaPolygon)
   		_arrFC.append(_pathManzanaPolygonUnion)
   		_arrFC.append(_pathManzanaUnion)

		arcpy.env.workspace = pathGDBTemp
   		for fc in _arrFC:
   			arcpy.Delete_management(fc)
   		
	except IOError as err:
		print("Error OS")


if __name__ == "__main__":
    main()