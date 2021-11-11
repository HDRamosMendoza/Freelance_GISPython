#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Name App 	: Hallar la áreas verdes de retiros de lotes
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

import arcpy
import os
import shutil

arcpy.SpatialReference(4326)
arcpy.env.workspace = os.path.join(os.getcwd(), 'SHP')
arr_retiro = [];
arr_merge  = [];

_inFC_LoteFrente = os.path.join(arcpy.env.workspace, "Frente_Lote.shp")
arcpy.MakeFeatureLayer_management(_inFC_LoteFrente, "TEMP_LoteFrente")
_inFC_LoteUrbano = os.path.join(arcpy.env.workspace, "Lote_urbano.shp")
arcpy.MakeFeatureLayer_management(_inFC_LoteUrbano, "TEMP_LoteUrbano")

def removeFile(path):
	if os.path.isdir(path):
		shutil.rmtree(path)
	os.makedirs(path)

def main():
	removeFile(os.path.join(arcpy.env.workspace, 'Producto'))
	with arcpy.da.SearchCursor("TEMP_LoteFrente", ["rv_retiro"]) as cursorRetiro:
		for row in cursorRetiro:
			if row[0] not in arr_retiro:
				arr_retiro.append(row[0])

	for _item in arr_retiro:
		arcpy.SelectLayerByAttribute_management(
			"TEMP_LoteFrente",
			"NEW_SELECTION",
			'"rv_retiro"={}'.format(_item)
		)

		arcpy.Buffer_analysis(
			in_features = "TEMP_LoteFrente",
			out_feature_class = os.path.join(
				arcpy.env.workspace,
				"LoteRetiro_{}".format(str(_item).replace('.0','').replace('.',''))
			),
			buffer_distance_or_field = "{} Meters".format(_item),
			line_side 		= "FULL",
			line_end_type 	= "ROUND",
			dissolve_option = "NONE",
			dissolve_field 	= "",
			method 			= "PLANAR"
		)

		arcpy.Clip_analysis(
			"TEMP_LoteUrbano",
			os.path.join(
				arcpy.env.workspace,
				"LoteRetiro_{}.shp".format(str(_item).replace('.0','').replace('.',''))
			),
			os.path.join(
				arcpy.env.workspace,
				"CLIP_LoteRetiro_{}".format(str(_item).replace('.0','').replace('.',''))
			),
		)

		arcpy.management.Delete(
			os.path.join(
				arcpy.env.workspace,
				"LoteRetiro_{}.shp".format(str(_item).replace('.0','').replace('.',''))
			)
		)
		

	for _item in arr_retiro:
		arr_merge.append(
			os.path.join(
				arcpy.env.workspace,
				"CLIP_LoteRetiro_{}.shp".format(str(_item).replace('.0','').replace('.',''))
			)
		)

	
	arcpy.Merge_management(
		arr_merge,
		os.path.join(
			arcpy.env.workspace,
			"Producto",
			"FINAL_LoteRetiro"
		)
	)

	for _item in arr_retiro:
		arcpy.management.Delete(
			os.path.join(
				arcpy.env.workspace,
				"CLIP_LoteRetiro_{}.shp".format(str(_item).replace('.0','').replace('.',''))
			)
		)

if __name__ == "__main__":
    main()