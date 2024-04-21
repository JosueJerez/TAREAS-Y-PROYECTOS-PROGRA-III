# API de Manejo de Registros

Esta es una API desarrollada en Flask para el manejo de registros utilizando una estructura de datos de Árbol AVL.

## Descripción

La API permite cargar registros desde un archivo CSV, insertar registros manualmente, buscar registros por identificador y obtener información sobre el grupo de desarrollo.

## Instalación

1. Clona el repositorio a tu máquina local:

    ```
    git clone https://github.com/tu-usuario/nombre-del-repo.git
    ```

2. Instala las dependencias necesarias:

    ```
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```
    python app.py
    ```

2. Accede a las diferentes rutas de la API utilizando un cliente HTTP o navegador web.

## Rutas Disponibles

- **POST /cargar_csv:** Carga registros desde un archivo CSV.

- **POST /insertar_registro:** Inserta un registro manualmente.

- **GET /buscar_registro/<identificador>:** Busca un registro por su identificador.

- **GET /info_grupo:** Obtiene información sobre el grupo de desarrollo.

## Formato del Archivo CSV

El archivo CSV debe tener las siguientes columnas:

- `Date Rptd`: Fecha reportada en formato `mm/dd/yyyy hh:mm:ss AM/PM`.
- `data`: Datos asociados al registro.

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios al repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Integrantes del Grupo, nombre, carnet, porcentaje de trabajo

- Josué Vinicio Jerez Gómez 9490-22-1479 100%
- Mario Roberto Rompich Yoc 9490-17-17052 100%


