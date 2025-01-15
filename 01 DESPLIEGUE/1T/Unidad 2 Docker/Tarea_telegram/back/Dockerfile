# Usar la imagen oficial de Python como base
FROM python:3.11-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app/

# Instalar las dependencias de Python desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde la app FastAPI estará disponible
EXPOSE 8001

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
