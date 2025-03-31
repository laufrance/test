# 104048-TP0-20251C-9521
Repositorio para el TP0 de la materia Metodos y Modelos de la Ingenieria de Software 2 (9521) - FIUBA

![Coverage](https://codecov.io/gh/laufrance/test/branch/main/graph/badge.svg)


## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Desafíos mas complicados del Proyecto](#desafíos-mas-complicados-del-proyecto)
3. [Pre-requisitos](#pre-requisitos)
4. [Formatting](#formatting)
5. [.env file](#archivo-env)
6. [Construcción de la imagen Docker](#construcción-de-la-imagen-docker)
7. [Ejecución del servicio Docker](#ejecución-del-servicio-docker)
8. [Guía de Pruebas](#guía-de-pruebas)

---

## Introducción
Este proyecto implementa una API REST-like para la gestión de cursos, siguiendo el diseño "Package by Layer Design" con capas: **Controller**, **Service**, **Router**, **Repository** y **Testing**. La API permite crear, listar, obtener y eliminar cursos, validando las entradas y utilizando una base de datos SQLite.

---

## Desafíos mas complicados del Proyecto
- Reestructuración a **Package by Layer Design** para mantener el código limpio y modular.
- Dockerización completa del backend con base de datos local en sqlite.
- Validación de la longitud de la descripción entre **50 y 255 caracteres**.

---

## Pre-requisitos
Para levantar el entorno de desarrollo, necesitarás:

- **Python 3.11 o superior**
```
sudo apt install python3
```
- **Pip**  
```
sudo apt-get install python3-pip
```
- **Docker**
```
sudo apt-get install docker.io
```

- **Docker Compose**
```
sudo apt-get install docker-compose
```

---

## Formatting

Para el formateo del codigo se uso la libreria Black. Se corrió el siguiente comando:
```
black .
```


---
## Archivo .env
Se debe crear un archivo .env con el mismo formato que el archivo .env.example
```
HOST=0.0.0.0
PORT=5000
ENVIRONMENT=development
```
Aqui se van a definir las variables de entorno a utilizarse, Host, Port y Environment.

---

## Construcción de la imagen Docker

Desde la raíz del proyecto, ejecuta:

```
sudo docker-compose down
sudo docker-compose build
```

---

## Ejecución del servicio Docker

Para levantar la API en el contenedor:

```
sudo docker-compose up
```

Luego, la API estará disponible en (Si el host elegido en el archivo .env es localhost y el puerto es 5000):
[http://localhost:5000](http://localhost:5000)

Si se elige otro host y otro puerto la ip seria _http://host:puerto_

---

## Guía de Pruebas

Las pruebas E2E están implementadas con la librería unittest (de Python).
Link a la documentación oficial: [unittest Documentation](https://docs.python.org/3/library/unittest.html)

Para correr los tests dentro del docker:

```
sudo docker exec -it 104048-tp0-20251c-9521_api_1 python tests/e2etesting.py 0.0.0.0 5000
```
_--host --port_

Para correr los tests fuera del docker:

```
python3 tests/e2etesting.py 0.0.0.0 5000
```
_--host --port_
