
## GOOGLE CLOUD FUNCTION WITH firestore

En el archivo main.py se escriben dos funciones en python para Google Cloud Functions

## Para desplegar en GC 🚀

gcloud functions deploy [Nombre funcion] --runtime python39 --trigger-http --allow-unauthenticated

El [Nombre funcion] debe tener el nombre de la funcion dentro del archivo main.py y con ese
mismo nombre se guardará en en GC Functions

documentación de despliegue local
https://cloud.google.com/functions/docs/deploying/filesystem?hl=es

Tambien existe un despliegue desdte github para investigar

Para registrar las credenciales de FireStore localmente, se debe crear una variable de entorno
con la ruta de la key .json que entrega la cuenta de servicio que se debe crear previamente

set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\deemd\Documents\keyServiceCountGC\laboratorio-01-317620-54050f53053a.json

### Pruebas locales con Pytest 📋

Dentro del proyecto para inicializar una copia virtual de una toda la instancia de python
py -m venv env

Para activar el entorno virtual en la linea de comandos
.\env\Scripts\activate

instalar paquetes individuales
pip install

Instalar todos los paquetes del archivo requeriments.txt
pip install -r requirements.txt

instalar dependencias para FireStore
pip install --upgrade google-cloud-firestore

Desactivar instancia virtual de python
deactivate

Para iniciar test
dentro del entorno virtual
pytest main_test.py
Tener instalado pytest

## Construido con 🛠️
* [Python]


## Autor
 ✒️
* **David Erira** - *Desarrollo* - [DEEM](https://github.com/DavidErira)

---
⌨️ con ❤️ por [DEEM](https://github.com/DavidErira) 
