# Se usa la versión slim con versión fija por buenas prácticas
FROM python:3.12-slim

# Creamos un directorio de trabajo en la imagen
WORKDIR /app

# Copiamos la carpeta html/ local al contenedor
COPY html/ /app/html/

# Exponemos el puerto 8080
EXPOSE 8080

# El comando principal que levanta el servidor HTTP apuntando a la carpeta html
CMD ["python3", "-m", "http.server", "8080", "--directory", "html"]