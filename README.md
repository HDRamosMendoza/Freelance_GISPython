# Freelance_GISPython
Repositorio de trabajos de automatización de freelance

>Name App : Calculo de angulos interiores

>Description: Se calcular los angulos interiores de un polígono.

>Created : Heber DANIEL Ramos Mendoza (HDRamosMendoza)

>Email: heber.daniel.ramos.mendoza@gmail.com

>Position : GIS Developer

>Location : Perú/Lima/San Juan de Lurigancho

>Social media : HDRamosMendoza

>Phone: 999130638

>Web: https://hdramosmendoza.github.io/Perfil-Profesional/

>Copyright: Heber Daniel Ramos Mendoza

>Licence: Favor de mencionar al autor

------------------------------------

- 1_CSV_DarFormatoXY. 
	
	>Paso 1: En el CSV modificamos las columnas longitud y latitud. Reemplazmos el texto por el signo negativo.

	>Paso 2: Del CSV exportamos a formato GEOJSON(JSON).

	>Paso 3: El archivo JSON reemplazamos la extención con .js y el el GEOJSON lo igualamos a un a una variable.
	
	>Paso 4: Construimos el mapa de leaflet y llamamos el el archivo .js(GEOJSON - JSON)
	
	https://hdramosmendoza.github.io/Freelance_GISPython/1_CSV_DarFormatoXY/MAP/index.html

- 2_JSON_SHP. 
	
	* Paso 1: Se extrae los datos del servicios.

	* Paso 2: Se reemplazamos la coma por el punto.

	* Paso 3: Convertimos de JSON a un .csv.
	
	* Paso 4: Se lleva de TABLE a .shp

	* Paso 5: Se comprime el .shp
	

- 3_Calculate_Angles. 
	
	* Paso 1: Ingresa el polígono.

	* Paso 2: Se crea una copia en menoria.

	* Paso 3: Se crea a partir de los vertices del polígono se crea puntos y se genera un radio de influencia.
	
	* Paso 4: Con el radio de influencia se dar corte con el polígono.

	* Paso 5: Se obtiene el área y con ello a traves de un regla de 3 simple directa se calcula el ángulo