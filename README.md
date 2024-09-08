# Pagina web Django+Angular

Hola :),

La pagina sigue en construccion y por algunos detalles inesperados el back-end y el front-end quedaron en repositorios separados.

# Installacion de django (back-end)

1.Installar python
https://www.python.org/downloads/ 

opcional
https://docs.python.org/3/tutorial/venv.html
 Es recomendado usar venv o Virtual Environment para installar django y los archivos de este proyecto para que queden aparte y no sean afectados por otros posibles packetes ya instalados en el computador.

en powershell, cdm o cli
 
Para crear un entorno virtual, decide en qué directorio deseas colocarlo y ejecuta el módulo `venv` como un script con la ruta del directorio:

```bash
python -m venv tutorial-env
```

Esto creará el directorio `tutorial-env` si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ubicación común para un entorno virtual es `.venv`. Este nombre mantiene el directorio típicamente oculto en tu shell y, por lo tanto, fuera del camino, mientras le da un nombre que explica por qué existe el directorio. También evita conflictos con archivos de definición de variables de entorno `.env` que algunas herramientas soportan.

Una vez que hayas creado un entorno virtual, puedes activarlo.

En Windows, ejecuta:

```bash
tutorial-env\Scripts\activate
```

con esto en la consola deveria verse el nombre del venv antes del directorio

2. instalar los componentes

 descargar el archivo requirements.txt

 y usar el commando
 ```bash
pip install -r .\requirements.txt
```
esto comenzara a installar todos los componentes usados para el backend

3. descargar proyecto

luego descargar la carpeta DjangoAPI

5. activar el proyecto

dentro de la carpeta de DjangoAPI usar:
```bash
...\> py manage.py runserver
```
esto hara que el servidor de backend quede arriba :)

# Instalacion de Angular (front-end)

1. instalr nodejs: https://nodejs.org/en
2. instalar angular
 ```bash
npm install -g @angular/cli
```
3.descargar todo el repositorio de angular18 que se encuentra en:https://github.com/carlosandresruiz1/angular18/tree/master (en un futuro espero poder dejarlo en uno solo repositorio)
4.dentro de la carpeta de angular18 usar:
 ```bash
ng serve
```
5.el servidor de angular debe estar funcionando en http://localhost:4200/

# CRUD + usuario y contraseña

- para acceder a las funciones de crud en la pagina principal (http://localhost:4200/) en la barra de navegacion se encutra la opcion de login, desde alli se puede seleccionar admin que nos llevara a la pagina de admistracion.
- las credenciales para esta son:User: Admin
  email: Admin123@gmail.com
  Password: Admin123

- desde all'i se puede admistrar la informacion que aparecera en la pagina.



