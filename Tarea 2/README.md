# Biblioteca Personal - Gestión de Libros con Python y SQLite

## 📚 Descripción del Proyecto

Aplicación de línea de comandos desarrollada en Python que permite administrar una biblioteca personal. La aplicación almacena información sobre los libros (título, autor, género y estado de lectura) en una base de datos SQLite.

### Características Principales

- ✅ Agregar nuevos libros con información completa
- ✅ Ver el listado completo de libros registrados
- ✅ Buscar libros por título, autor o género
- ✅ Actualizar información de libros existentes
- ✅ Eliminar libros del sistema
- ✅ Ver estadísticas de la biblioteca
- ✅ Interfaz interactiva en consola
- ✅ Base de datos persistente con SQLite

---

## 🛠️ Requisitos Técnicos

- **Python**: 3.6 o superior
- **SQLite3**: Incluido en Python por defecto
- **Sistema Operativo**: Windows, macOS o Linux

---

## 📦 Estructura del Proyecto

```
biblioteca-personal/
│
├── main.py              # Punto de entrada de la aplicación
├── app.py               # Lógica del menú interactivo
├── database.py          # Gestión de la base de datos SQLite
├── models.py            # Definición del modelo Libro
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Este archivo
└── .gitignore           # Archivos a ignorar en Git
```

### Descripción de Archivos

| Archivo | Función |
|---------|---------|
| `main.py` | Punto de entrada que inicializa la aplicación |
| `app.py` | Contiene la clase `BibliotecaApp` con el menú y lógica de interacción |
| `database.py` | Clase `BaseDatos` que gestiona todas las operaciones CRUD con SQLite |
| `models.py` | Clase `Libro` que define la estructura de un libro |
| `requirements.txt` | Lista de dependencias (opcional, el proyecto no tiene dependencias externas) |

---

## 🚀 Instrucciones de Ejecución

### 1. En PyCharm

#### Opción A: Usar PyCharm IDE
1. Abre PyCharm
2. Selecciona `File` → `Open` y elige la carpeta del proyecto
3. En la ventana de proyecto, haz clic derecho en `main.py`
4. Selecciona `Run 'main'`

#### Opción B: Usar la terminal integrada de PyCharm
1. Abre la terminal integrada (`View` → `Tool Windows` → `Terminal`)
2. Ejecuta:
   ```bash
   python main.py
   ```

### 2. En una Terminal/CMD

```bash
# Navega a la carpeta del proyecto
cd ruta/al/proyecto

# Ejecuta la aplicación
python main.py
```

---

## 📖 Uso de la Aplicación

### Menú Principal

Una vez ejecutado el programa, verás el siguiente menú:

```
==================================================
          BIBLIOTECA PERSONAL
==================================================
1. Agregar nuevo libro
2. Ver todos los libros
3. Buscar libro
4. Actualizar libro
5. Eliminar libro
6. Ver estadísticas
7. Salir
==================================================
```

### Explicación de Opciones

#### 1. Agregar nuevo libro
- Solicita: Título, Autor, Género, Estado de lectura
- Registra el libro en la base de datos

#### 2. Ver todos los libros
- Muestra una lista numerada de todos los libros registrados
- Cada libro muestra: ID, Título, Autor, Género, Estado

#### 3. Buscar libro
- Permite buscar por:
  - Título (búsqueda parcial)
  - Autor
  - Género
- Muestra los resultados coincidentes

#### 4. Actualizar libro
- Selecciona un libro por su ID
- Permite modificar cualquier campo (título, autor, género, estado)
- Deja los campos en blanco para mantener los valores actuales

#### 5. Eliminar libro
- Solicita confirmación antes de eliminar
- El libro se elimina permanentemente de la base de datos

#### 6. Ver estadísticas
- Muestra:
  - Total de libros
  - Cantidad de libros leídos
  - Cantidad de libros no leídos
  - Porcentaje de libros leídos

#### 7. Salir
- Cierra la conexión a la base de datos
- Termina la aplicación

---

## 💾 Almacenamiento de Datos

La base de datos se crea automáticamente en la primera ejecución:

- **Nombre**: `biblioteca.db`
- **Ubicación**: Misma carpeta donde se ejecuta `main.py`
- **Tabla**: `libros` con los campos:
  - `id` (INTEGER, clave primaria, autoincremento)
  - `titulo` (TEXT)
  - `autor` (TEXT)
  - `genero` (TEXT)
  - `leido` (BOOLEAN)

---

## 🔍 Ejemplo de Uso

### Sesión típica:

```
1. Seleccionar opción 1 (Agregar libro)
   - Título: "El Quijote"
   - Autor: "Miguel de Cervantes"
   - Género: "Novela"
   - ¿Ya lo has leído?: "s" (sí)

2. Seleccionar opción 2 (Ver todos los libros)
   - [1] El Quijote | Miguel de Cervantes | Novela | ✓ Leído

3. Seleccionar opción 3 (Buscar)
   - Buscar por: 1 (Título)
   - Ingresa el título: "Quijote"
   - Resultado: [1] El Quijote | Miguel de Cervantes | Novela | ✓ Leído

4. Seleccionar opción 6 (Estadísticas)
   - Total de libros: 1
   - Libros leídos: 1
   - Libros no leídos: 0
   - Porcentaje de libros leídos: 100.0%
```

---

## 🎨 Características de Diseño

### Modularización
El código está organizado en módulos independientes:
- **models.py**: Define la estructura de datos
- **database.py**: Gestiona la persistencia
- **app.py**: Maneja la lógica de la aplicación
- **main.py**: Punto de entrada

### Validación de Entrada
- Validación de campos requeridos
- Confirmación antes de operaciones destructivas (eliminar)
- Manejo de errores de base de datos

### Interfaz Amigable
- Menús claros y bien estructurados
- Mensajes informativos (✓ para éxito, ✗ para errores)
- Pausas entre operaciones para legibilidad

---

## 🐛 Manejo de Errores

La aplicación incluye:
- Try-catch para errores de base de datos
- Validación de entrada del usuario
- Manejo de conexiones seguras
- Mensajes de error descriptivos

---

## 📝 Notas Importantes

- La base de datos se persiste entre sesiones
- Todos los datos se almacenan localmente en `biblioteca.db`
- No requiere conexión a internet
- Compatible con Python 3.6+
- Funciona en Windows, macOS y Linux

---

## 🔧 Posibles Mejoras Futuras

- Exportar/importar datos a CSV o JSON
- Interfaz gráfica con Tkinter
- Estadísticas avanzadas (libros por género, por autor)
- Calificación de libros (1-5 estrellas)
- Fecha de adición y fecha de lectura
- Búsqueda avanzada con múltiples criterios

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autor

Desarrollado como proyecto académico para la Licenciatura en Ingeniería en Sistemas Computacionales.

---

## ❓ Preguntas Frecuentes

**P: ¿Dónde se guarda la base de datos?**
R: Se guarda en el mismo directorio donde ejecutas `main.py` con el nombre `biblioteca.db`.

**P: ¿Puedo eliminar `biblioteca.db`?**
R: Sí, pero perderás todos los datos. Se creará una nueva base de datos vacía en la próxima ejecución.

**P: ¿Cómo hago una copia de seguridad?**
R: Simplemente copia el archivo `biblioteca.db` a otra ubicación.

**P: ¿Puedo usar este código en otro proyecto?**
R: Sí, está disponible bajo licencia MIT.

---
