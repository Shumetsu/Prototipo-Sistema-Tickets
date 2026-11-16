from django.shortcuts import render


def inicio(request):
    """Panel de demostración: los tickets son datos de muestra, sin persistencia."""
    tickets = [
        {"id": "TK-1048", "title": "No puedo acceder a mi cuenta", "requester": "Camila Rojas", "email": "camila.rojas@empresa.cl", "team": "Acceso y cuentas", "priority": "Alta", "status": "Abierto", "date": "Hoy, 09:42", "initials": "CR", "color": "lavender", "description": "Desde esta mañana no puedo iniciar sesión. El sistema indica que mi contraseña es incorrecta, pero ya la restablecí dos veces."},
        {"id": "TK-1047", "title": "Solicitud de acceso a carpeta compartida", "requester": "Diego Muñoz", "email": "diego.munoz@empresa.cl", "team": "Permisos", "priority": "Media", "status": "En progreso", "date": "Hoy, 09:18", "initials": "DM", "color": "blue", "description": "Necesito acceso de lectura a la carpeta Proyectos 2026 para preparar el informe mensual."},
        {"id": "TK-1046", "title": "Monitor con pantalla parpadeante", "requester": "Fernanda Silva", "email": "fernanda.silva@empresa.cl", "team": "Hardware", "priority": "Media", "status": "En progreso", "date": "Hoy, 08:56", "initials": "FS", "color": "pink", "description": "La pantalla parpadea de forma intermitente, especialmente al conectar el notebook a la base."},
        {"id": "TK-1045", "title": "Error al generar reporte de ventas", "requester": "Matías Pérez", "email": "matias.perez@empresa.cl", "team": "Aplicaciones", "priority": "Urgente", "status": "Abierto", "date": "Ayer, 16:30", "initials": "MP", "color": "mint", "description": "Al exportar el reporte de ventas de octubre aparece un error y el archivo queda vacío. Lo necesitamos para el cierre."},
        {"id": "TK-1044", "title": "Configurar correo en nuevo teléfono", "requester": "Valentina Soto", "email": "valentina.soto@empresa.cl", "team": "Dispositivos", "priority": "Baja", "status": "Resuelto", "date": "Ayer, 15:12", "initials": "VS", "color": "peach", "description": "Cambié mi teléfono y necesito volver a configurar el correo corporativo."},
        {"id": "TK-1043", "title": "VPN se desconecta al trabajar desde casa", "requester": "Javier Torres", "email": "javier.torres@empresa.cl", "team": "Redes", "priority": "Alta", "status": "Abierto", "date": "Ayer, 14:05", "initials": "JT", "color": "yellow", "description": "La conexión VPN se cae cada 10 o 15 minutos y debo conectarme nuevamente."},
        {"id": "TK-1042", "title": "Instalación de herramienta de diseño", "requester": "Antonia Vega", "email": "antonia.vega@empresa.cl", "team": "Aplicaciones", "priority": "Baja", "status": "Resuelto", "date": "Ayer, 11:40", "initials": "AV", "color": "lilac", "description": "Solicito instalar la herramienta de diseño aprobada para el equipo de Marketing."},
    ]
    return render(request, "inicio.html", {"tickets": tickets})
