# 🎥🌤️Movie Weather App

## Descripción

Esta aplicación utiliza FastAPI para integrar dos APIs externas: la API de la Base de Datos de Películas y la API de Open-Meteo. La aplicación permite buscar información de películas y obtener datos meteorológicos basados en la fecha de lanzamiento de la película.

## ⚙️Configuración

### Requisitos

- Python 3.12.7
- Dependencias listadas en `requirements.txt`

### 🛠️Instalación

Clona este repositorio y ejecuta el siguiente comando para instalar las dependencias:

```
pip install -r requirements.txt
```

### Ejecución Local

Para iniciar el servidor, ejecuta:

```
uvicorn src.main:app --reload`
```

### 🐳📦Ejecucion con Docker

#### Desarrollo

Para iniciar el entorno de desarrollo utilizando Docker, asegúrate de tener Docker y Docker Compose instalados, y luego ejecuta:

```
docker-compose -f docker-compose.dev.yml up
```

Esto construirá la imagen usando `Dockerfile.dev` y levantará el servicio definido en `docker-compose.dev.yml`. Puedes acceder a la aplicación en `localhost:8000`.

#### Producción

Para desplegar la aplicación en producción, utiliza:

```
docker-compose up
```

### 💻 Uso

Esto usará `Dockerfile` para construir la imagen en un entorno optimizado para producción. Asegúrate de que todos los puertos y configuraciones estén ajustados como necesitas en tu entorno de producción.

### 📈Documentación API

Independientemente del entorno, puedes acceder a la documentación interactiva de FastAPI y probar la API navegando a `localhost:8000/docs` después de que el servidor esté corriendo.

Puedes usar el archivo `api.http` con la extensión REST Client de tu editor para realizar solicitudes directamente desde tu IDE. Alternativamente, puedes acceder a la documentación interactiva de FastAPI para probar la API navegando a `localhost:8000/api/v1/docs` después de iniciar el servidor.

Accede a `localhost:8000/movie-weather?title={movie_title}` para obtener los datos combinados de película y clima.


## 🧪Ejecutar Tests

Para ejecutar los tests, utiliza el comando `pytest` en la terminal. Esto ejecutará todas las pruebas definidas en el directorio `tests`. Si deseas ejecutar pruebas específicas, proporciona la ruta al archivo de tests. Para un informe de cobertura de código, agrega la opción `--cov=src`. Asegúrate de haber instalado las dependencias de desarrollo con `pip install -r requirements-dev.txt`.

## 📚Estructura de Archivos

- `src/main.py`: Punto de entrada de la aplicación.
- `src/controllers/`: Controladores que manejan las rutas de la API.
- `src/services/`: Servicios que contienen la lógica de negocio.
- `src/schemas/`: Esquemas Pydantic para validación de datos.

## 👥Contribuir

Para contribuir al proyecto, envía un pull request o abre un issue para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo la licencia MIT.
