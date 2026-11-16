# Prototipo de sistema de tickets

Panel de soporte demostrativo hecho con Django. Incluye tickets de ejemplo, búsqueda, filtros, creación simulada de solicitudes y cambio de estado en la interfaz.

Los datos se guardan solo en la página abierta y se restablecen al recargar. El prototipo no requiere migraciones ni crea usuarios.

## Ejecutar localmente

1. Instala Python 3.10 o posterior.
2. En esta carpeta, crea y activa un entorno virtual si lo deseas.
3. Instala dependencias: `python -m pip install -r requirements.txt`
4. Inicia el servidor: `python manage.py runserver`
5. Abre `http://127.0.0.1:8000/`.

Es una maqueta para presentar y probar el flujo visual; no está preparada para uso en producción.
