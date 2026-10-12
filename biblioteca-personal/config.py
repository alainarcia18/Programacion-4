"""
Configuración de conexión a MariaDB
Define la cadena de conexión y configuraciones de SQLAlchemy
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de MariaDB
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root123')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'biblioteca_personal')

# Construir la cadena de conexión
# Formato: mysql+pymysql://usuario:contraseña@host:puerto/base_datos
if DB_PASSWORD:
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    DATABASE_URL = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Configuración de SQLAlchemy
SQLALCHEMY_CONFIG = {
    'echo': False,  # Cambiar a True para ver las consultas SQL
    'pool_pre_ping': True,  # Verificar la conexión antes de usarla
    'pool_recycle': 3600,  # Reciclar conexiones cada hora
}

print(f"Cadena de conexión: {DATABASE_URL}")
