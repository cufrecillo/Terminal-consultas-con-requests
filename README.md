# Terminal_consultas_con_requests
### Ejercicio que simula una terminal con diferentes opciones de búsqueda con la libreria request, para no trabajar todo el tiempo con una BBDD en local.

https://restcountries.eu/

https://requests.readthedocs.io/en/master/

Instalar la librería requests

Hacer una request a la url que nos traiga todos los países del mundo

1. Crear una pequeña aplicación con las siguientes características:

  - Buscar país

    * Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitirá los siguientes valores: name, capital, region,   population, area, idioma (el primero), flag A su vez estos valores acturán como cabeceros
 
  - Buscar continente

    * Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico EJ. dinámico --> Si se busca     "africa", el archivo deberá llamarse --> africa.json
    * Además entregar la población total del continente
  
  - Paises por idioma

      * Devolver una lista con todos los paises que hablan el idioma indicado por el usuario
  
  - Descargar bandera

      * Permita al usuario descargar la bandera del país que quiera.
      * Estas imágenes serán guardadas en una carpeta aparte con el nombre del país
  
  - Historial

      * Devolvera una lista de los paises buscados de la siguiente manera:
      * name: value - population: value
  
2. Encontrar los 10 paises más grandes

3. Encontrar los 10 paises más densamente poblados

4. ¿Cuál es el idioma oficial más hablado?
