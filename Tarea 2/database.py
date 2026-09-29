# -*- coding: utf-8 -*-
"""
Módulo de base de datos para la aplicación de biblioteca.
Gestiona todas las operaciones CRUD con SQLite.
"""

import sqlite3
from models import Libro


class BaseDatos:
    """Gestiona la conexión y operaciones con la base de datos SQLite."""
    
    def __init__(self, nombre_db="biblioteca.db"):
        """
        Inicializa la conexión a la base de datos.
        
        Args:
            nombre_db (str): Nombre del archivo de base de datos
        """
        self.nombre_db = nombre_db
        self.conexion = None
        self.cursor = None
        self.conectar()
        self.crear_tabla()
    
    def conectar(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conexion = sqlite3.connect(self.nombre_db)
            self.cursor = self.conexion.cursor()
            print(f"✓ Conexión a base de datos '{self.nombre_db}' establecida.")
        except sqlite3.Error as e:
            print(f"✗ Error al conectar a la base de datos: {e}")
    
    def crear_tabla(self):
        """Crea la tabla de libros si no existe."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    leido BOOLEAN DEFAULT 0
                )
            ''')
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"✗ Error al crear la tabla: {e}")
    
    def agregar_libro(self, titulo, autor, genero, leido=False):
        """
        Agrega un nuevo libro a la base de datos.
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            genero (str): Género del libro
            leido (bool): Estado de lectura
            
        Returns:
            bool: True si se agregó exitosamente, False en caso contrario
        """
        try:
            self.cursor.execute('''
                INSERT INTO libros (titulo, autor, genero, leido)
                VALUES (?, ?, ?, ?)
            ''', (titulo, autor, genero, int(leido)))
            self.conexion.commit()
            print(f"✓ Libro '{titulo}' agregado exitosamente.")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error al agregar el libro: {e}")
            return False
    
    def obtener_todos_libros(self):
        """
        Obtiene todos los libros de la base de datos.
        
        Returns:
            list: Lista de objetos Libro
        """
        try:
            self.cursor.execute('SELECT id, titulo, autor, genero, leido FROM libros ORDER BY id')
            resultados = self.cursor.fetchall()
            libros = [Libro(row[0], row[1], row[2], row[3], bool(row[4])) for row in resultados]
            return libros
        except sqlite3.Error as e:
            print(f"✗ Error al obtener libros: {e}")
            return []
    
    def obtener_libro_por_id(self, libro_id):
        """
        Obtiene un libro específico por su ID.
        
        Args:
            libro_id (int): ID del libro
            
        Returns:
            Libro: Objeto Libro o None si no existe
        """
        try:
            self.cursor.execute(
                'SELECT id, titulo, autor, genero, leido FROM libros WHERE id = ?',
                (libro_id,)
            )
            resultado = self.cursor.fetchone()
            if resultado:
                return Libro(resultado[0], resultado[1], resultado[2], resultado[3], bool(resultado[4]))
            return None
        except sqlite3.Error as e:
            print(f"✗ Error al obtener el libro: {e}")
            return None
    
    def buscar_libros(self, criterio, valor):
        """
        Busca libros según un criterio (título, autor o género).
        
        Args:
            criterio (str): Campo a buscar ('titulo', 'autor', 'genero')
            valor (str): Valor a buscar
            
        Returns:
            list: Lista de objetos Libro que coinciden
        """
        try:
            criterios_validos = ['titulo', 'autor', 'genero']
            if criterio not in criterios_validos:
                print(f"✗ Criterio inválido. Use: {', '.join(criterios_validos)}")
                return []
            
            consulta = f'SELECT id, titulo, autor, genero, leido FROM libros WHERE {criterio} LIKE ? ORDER BY id'
            self.cursor.execute(consulta, (f'%{valor}%',))
            resultados = self.cursor.fetchall()
            libros = [Libro(row[0], row[1], row[2], row[3], bool(row[4])) for row in resultados]
            return libros
        except sqlite3.Error as e:
            print(f"✗ Error en la búsqueda: {e}")
            return []
    
    def actualizar_libro(self, libro_id, titulo=None, autor=None, genero=None, leido=None):
        """
        Actualiza la información de un libro.
        
        Args:
            libro_id (int): ID del libro a actualizar
            titulo (str): Nuevo título (opcional)
            autor (str): Nuevo autor (opcional)
            genero (str): Nuevo género (opcional)
            leido (bool): Nuevo estado de lectura (opcional)
            
        Returns:
            bool: True si se actualizó exitosamente, False en caso contrario
        """
        try:
            # Obtener el libro actual
            libro = self.obtener_libro_por_id(libro_id)
            if not libro:
                print(f"✗ No se encontró el libro con ID {libro_id}")
                return False
            
            # Usar los valores actuales si no se proporcionan nuevos
            titulo = titulo if titulo is not None else libro.titulo
            autor = autor if autor is not None else libro.autor
            genero = genero if genero is not None else libro.genero
            leido = leido if leido is not None else libro.leido
            
            self.cursor.execute('''
                UPDATE libros
                SET titulo = ?, autor = ?, genero = ?, leido = ?
                WHERE id = ?
            ''', (titulo, autor, genero, int(leido), libro_id))
            self.conexion.commit()
            print(f"✓ Libro con ID {libro_id} actualizado exitosamente.")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error al actualizar el libro: {e}")
            return False
    
    def eliminar_libro(self, libro_id):
        """
        Elimina un libro de la base de datos.
        
        Args:
            libro_id (int): ID del libro a eliminar
            
        Returns:
            bool: True si se eliminó exitosamente, False en caso contrario
        """
        try:
            libro = self.obtener_libro_por_id(libro_id)
            if not libro:
                print(f"✗ No se encontró el libro con ID {libro_id}")
                return False
            
            self.cursor.execute('DELETE FROM libros WHERE id = ?', (libro_id,))
            self.conexion.commit()
            print(f"✓ Libro '{libro.titulo}' eliminado exitosamente.")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error al eliminar el libro: {e}")
            return False
    
    def contar_libros(self):
        """
        Cuenta el número total de libros en la base de datos.
        
        Returns:
            int: Cantidad de libros
        """
        try:
            self.cursor.execute('SELECT COUNT(*) FROM libros')
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"✗ Error al contar libros: {e}")
            return 0
    
    def contar_libros_leidos(self):
        """
        Cuenta el número de libros ya leídos.
        
        Returns:
            int: Cantidad de libros leídos
        """
        try:
            self.cursor.execute('SELECT COUNT(*) FROM libros WHERE leido = 1')
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"✗ Error al contar libros leídos: {e}")
            return 0
    
    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion:
            self.conexion.close()
            print("✓ Conexión a base de datos cerrada.")
