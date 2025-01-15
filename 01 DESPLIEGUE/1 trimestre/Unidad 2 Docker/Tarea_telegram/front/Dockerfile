# Usar una imagen base de Nginx
FROM nginx:alpine

# Copiar el archivo HTML y el script JavaScript al directorio de Nginx
COPY .  /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto para ejecutar Nginx
CMD ["nginx", "-g", "daemon off;"]