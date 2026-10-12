# Biblioteca Personal
📚 Biblioteca Personal - MariaDB + SQLAlchemy

Una aplicación de consola para gestionar una biblioteca personal utilizando MariaDB como base de datos y SQLAlchemy como ORM (Object-Relational Mapping).

🎯 Características
✅ Agregar nuevos libros
✅ Ver listado completo de libros
✅ Buscar libros por título, autor o género
✅ Actualizar información de libros
✅ Eliminar libros
✅ Ver estadísticas de la biblioteca
✅ Interfaz amigable en consola
✅ Manejo robusto de excepciones
📋 Requisitos Previos
Python 3.8 o superior
MariaDB 10.5 o superior
pip (gestor de paquetes de Python)
🔧 Instalación
1️⃣ Instalar MariaDB
En Windows:
Descarga el instalador desde mariadb.org/download
Ejecuta el instalador .msi
Durante la instalación:
IMPORTANTE: Establece una contraseña para el usuario root
Selecciona "Install as a service"
Anota la contraseña que estableciste
Reinicia tu computadora
Verifica la instalación abriendo CMD:
cmd
   mariadb --version
En macOS:
bash
# Instalar con Homebrew
brew install mariadb

# Iniciar el servicio
brew services start mariadb

# Asegurar la instalación (opcional)
mysql_secure_installation
En Linux (Ubuntu/Debian):
bash
# Instalar MariaDB
sudo apt-get update
sudo apt-get install mariadb-server

# Iniciar el servicio
sudo systemctl start mariadb

# Verificar instalación
mariadb --version
2️⃣ Clonar el Repositorio
bash
git clone https://github.com/TU_USUARIO/Programacion-4.git
cd Programacion-4/biblioteca-personal
3️⃣ Crear Entorno Virtual
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Deberías ver (venv) al inicio de tu terminal.

4️⃣ Instalar Dependencias
bash
pip install -r requirements.txt

Se instalarán:

SQLAlchemy==2.0.23 (ORM)
PyMySQL==1.1.0 (Driver MariaDB)
python-dotenv==1.0.0 (Variables de entorno)
5️⃣ Configurar la Cadena de Conexión
Opción A: Usando archivo .env (Recomendado)
Copia el archivo .env.example a .env:
bash
   cp .env.example .env
Edita .env con tus credenciales de MariaDB:
   DB_USER=root
   DB_PASSWORD=tu_contraseña_aqui
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=biblioteca_personal
Guarda el archivo
Opción B: Editar directamente en config.py

Si no quieres usar .env, edita config.py:

python
DB_USER = "root"
DB_PASSWORD = "tu_contraseña"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "biblioteca_personal"
6️⃣ Crear la Base de Datos y Tabla
Opción A: Usando el script SQL (Automático)
bash
# Windows
"C:\Program Files\MariaDB 13.0\bin\mariadb.exe" -u root -p < setup_database.sql

# macOS/Linux
mariadb -u root -p < setup_database.sql

Te pedirá la contraseña. Ingrésala.

Opción B: Manualmente
Conectate a MariaDB:
bash
   mariadb -u root -p
Ejecuta estos comandos SQL:
sql
   CREATE DATABASE IF NOT EXISTS biblioteca_personal;
   
   USE biblioteca_personal;
   
   CREATE TABLE IF NOT EXISTS libros (
       id INT AUTO_INCREMENT PRIMARY KEY,
       titulo VARCHAR(255) NOT NULL,
       autor VARCHAR(255) NOT NULL,
       genero VARCHAR(100) NOT NULL,
       leido BOOLEAN DEFAULT FALSE,
       fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
       fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
       INDEX idx_titulo (titulo),
       INDEX idx_autor (autor)
   );
   
   EXIT;
🚀 Ejecutar la Aplicación

Con el entorno virtual activado (venv), ejecuta:

bash
python main.py

Deberías ver el menú principal:

═════════════════════════════════════════════════════════════
                  📚 BIBLIOTECA PERSONAL 📚
═════════════════════════════════════════════════════════════

¿Qué deseas hacer?

1. Agregar nuevo libro
2. Ver todos los libros
3. Buscar libro
4. Actualizar información de un libro
5. Eliminar un libro
6. Ver estadísticas
7. Salir

═════════════════════════════════════════════════════════════
Selecciona una opción (1-7):
📁 Estructura del Proyecto
biblioteca-personal/
├── main.py                 # Aplicación principal
├── models.py              # Modelos SQLAlchemy
├── database_service.py    # Operaciones CRUD
├── config.py              # Configuración
├── utils.py               # Herramientas auxiliares
├── requirements.txt       # Dependencias
├── .env                   # Variables de entorno (NO subir a GitHub)
├── .env.example          # Template de .env
├── setup_database.sql    # Script de setup
├── .gitignore            # Archivos a ignorar
└── README.md             # Este archivo
🎯 Ejemplo de Uso
Agregar un libro:
Selecciona una opción (1-7): 1

➕ AGREGAR NUEVO LIBRO

Título del libro: El Quijote
Autor del libro: Miguel de Cervantes
Género del libro: Novela clásica
¿Ya lo has leído? (s/n): s

✓ Libro 'El Quijote' agregado correctamente (ID: 1)
Ver todos los libros:
Selecciona una opción (1-7): 2

📖 LISTADO DE TODOS LOS LIBROS

Se encontraron 1 libro(s)

ID: 1
Título: El Quijote
Autor: Miguel de Cervantes
Género: Novela clásica
Estado: Leído
🔐 Seguridad
✅ Variables de entorno para credenciales (archivo .env)
✅ Archivo .gitignore para NO versionar datos sensibles
✅ SQLAlchemy protege de SQL injection
✅ Validación de datos en todos los niveles
Importante:
NUNCA subas el archivo .env con contraseñas reales a GitHub
Usa .env.example como template
Agrega .env a .gitignore (ya está incluido)
🐛 Solución de Problemas
Problema	Solución
"mariadb not found"	Instala MariaDB o agrega al PATH
"ERROR 1045: Access denied"	Verifica contraseña en .env
"ERROR 1049: Unknown database"	Ejecuta el script SQL: setup_database.sql
"ModuleNotFoundError"	Activa entorno virtual y ejecuta pip install -r requirements.txt
"Database connection error"	Verifica que MariaDB esté corriendo
📊 Dependencias
SQLAlchemy==2.0.23      # ORM para Python
PyMySQL==1.1.0           # Driver MySQL/MariaDB
python-dotenv==1.0.0     # Cargar variables de entorno
📚 Estructura de la Base de Datos
Tabla: libros
Campo	Tipo	Descripción
id	INT	ID único (clave primaria)
titulo	VARCHAR(255)	Título del libro
autor	VARCHAR(255)	Nombre del autor
genero	VARCHAR(100)	Género literario
leido	BOOLEAN	¿Leído o no?
fecha_creacion	DATETIME	Cuándo se agregó
fecha_actualizacion	DATETIME	Última modificación
✨ Características Técnicas
✅ ORM con SQLAlchemy (mapeo objeto-relacional)
✅ Patrón de Servicio (separación de capas)
✅ Manejo robusto de excepciones
✅ Validación de entrada de datos
✅ Índices en BD para mejor performance
✅ Timestamps automáticos
✅ Búsquedas case-insensitive
📖 Documentación Adicional

Para más información sobre cómo funcionan los diferentes componentes:

models.py - Define la estructura de datos con SQLAlchemy
database_service.py - Contiene todas las operaciones CRUD
config.py - Configuración de conexión a MariaDB
main.py - Interfaz de usuario en consola
🎓 Conceptos Aprendidos

Este proyecto demuestra:

ORM con SQLAlchemy
Conexión a bases de datos relacionales
Patrones de diseño (Service pattern)
Manejo de excepciones
Validación de datos
Variables de entorno
📝 Licencia

Este proyecto es de uso educativo. Libre para usar, modificar y distribuir.

👨‍💻 Autor

Desarrollado como proyecto educativo para aprender SQLAlchemy y MariaDB.

✅ Checklist de Instalación

Antes de ejecutar, verifica:

 Python 3.8+ instalado
 MariaDB instalado y corriendo
 Entorno virtual creado y activado
 Dependencias instaladas (pip install -r requirements.txt)
 Archivo .env configurado con credenciales
 Base de datos biblioteca_personal creada
 Script setup_database.sql ejecutado
 Archivo config.py con configuración correcta

Si todo está ✓, ejecuta: python main.py
