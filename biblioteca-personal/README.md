# Biblioteca Personal
# 📚 Biblioteca Personal - MariaDB + SQLAlchemy

Una aplicación de consola para gestionar una biblioteca personal utilizando **MariaDB** como base de datos y **SQLAlchemy** como ORM (Object-Relational Mapping).

## 🎯 Características

- ✅ Agregar nuevos libros
- ✅ Ver listado completo de libros
- ✅ Buscar libros por título, autor o género
- ✅ Actualizar información de libros
- ✅ Eliminar libros
- ✅ Ver estadísticas de la biblioteca
- ✅ Interfaz amigable en consola
- ✅ Manejo robusto de excepciones

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- MariaDB 10.5 o superior
- pip (gestor de paquetes de Python)

---

## 🔧 Instalación

### 1️⃣ Instalar MariaDB

#### En Windows:
1. Descarga el instalador desde [mariadb.org/download](https://mariadb.org/download)
2. Ejecuta el instalador `.msi`
3. Durante la instalación:
   - **IMPORTANTE:** Establece una contraseña para el usuario `root`
   - Selecciona "Install as a service"
   - Anota la contraseña que estableciste
4. Reinicia tu computadora
5. Verifica la instalación abriendo CMD:
```cmd
   mariadb --version
```

#### En macOS:
```bash
# Instalar con Homebrew
brew install mariadb

# Iniciar el servicio
brew services start mariadb

# Asegurar la instalación (opcional)
mysql_secure_installation
```

#### En Linux (Ubuntu/Debian):
```bash
# Instalar MariaDB
sudo apt-get update
sudo apt-get install mariadb-server

# Iniciar el servicio
sudo systemctl start mariadb

# Verificar instalación
mariadb --version
```

---

### 2️⃣ Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/Programacion-4.git
cd Programacion-4/biblioteca-personal
```

---

### 3️⃣ Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu terminal.

---

### 4️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

Se instalarán:
- SQLAlchemy==2.0.23 (ORM)
- PyMySQL==1.1.0 (Driver MariaDB)
- python-dotenv==1.0.0 (Variables de entorno)

---

### 5️⃣ Configurar la Cadena de Conexión

#### Opción A: Usando archivo .env (Recomendado)

1. Copia el archivo `.env.example` a `.env`:
```bash
   cp .env.example .env
```

2. Edita `.env` con tus credenciales de MariaDB:
   
DB_USER=root
DB_PASSWORD=tu_contraseña_aqui
DB_HOST=localhost
DB_PORT=3306
DB_NAME=biblioteca_personal   


3. Guarda el archivo

#### Opción B: Editar directamente en config.py

Si no quieres usar `.env`, edita `config.py`:
```python
DB_USER = "root"
DB_PASSWORD = "tu_contraseña"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "biblioteca_personal"
```

---

### 6️⃣ Crear la Base de Datos y Tabla

#### Opción A: Usando el script SQL (Automático)

```bash
# Windows
"C:\Program Files\MariaDB 13.0\bin\mariadb.exe" -u root -p < setup_database.sql

# macOS/Linux
mariadb -u root -p < setup_database.sql
```

Te pedirá la contraseña. Ingrésala.

#### Opción B: Manually

1. Conectate a MariaDB:
```bash
   mariadb -u root -p
```

2. Ejecuta estos comandos SQL:
```sql
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
```

---

## 🚀 Ejecutar la Aplicación

Con el entorno virtual activado `(venv)`, ejecuta:

```bash
python main.py
```

Deberías ver el menú principal:
═════════════════════════════════════════════════════════════
📚 BIBLIOTECA PERSONAL 📚
═════════════════════════════════════════════════════════════

¿Qué deseas hacer?

Agregar nuevo libro
Ver todos los libros
Buscar libro
Actualizar información de un libro
Eliminar un libro
Ver estadísticas
Salir

═════════════════════════════════════════════════════════════
Selecciona una opción (1-7):

