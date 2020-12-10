# korea-weather-data-script

Script utilizado para combinar los datos meteorológicos de la República de Corea disponibles en https://data.kma.go.kr.

## Uso

```python  weather-data-script.py CARPETA``` donde ```CARPETA``` es la raíz que apunta a los datos descargados.

## Dependencias

Ninguna, el script hace uso de ```pathlib``` y ```csv``` únicamente.

## To Do

* Ordenar los datos por ```timestamp```, preferiblemente sin usar ```pandas``` para aumentar su portabilidad.
* Limpiar el código
* Diseñar/pulir la documentación
