# -*- coding: utf-8 -*-
"""
Script para cargar datos de ejemplo en la base de datos.
Ejecutar este script solo una vez para poblar la BD con libros de ejemplo.

Uso: python datos_ejemplo.py
"""

from database import BaseDatos


def cargar_datos_ejemplo():
    """Carga una lista de libros de ejemplo en la base de datos."""
    
    db = BaseDatos("biblioteca.db")
    
    # Lista de libros de ejemplo
    libros_ejemplo = [
        ("El Quijote", "Miguel de Cervantes", "Novela clásica", True),
        ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", True),
        ("1984", "George Orwell", "Distopía", False),
        ("Orgullo y prejuicio", "Jane Austen", "Romance", True),
        ("El Principito", "Antoine de Saint-Exupéry", "Fábula", True),
        ("Los miserables", "Víctor Hugo", "Novela histórica", False),
        ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", True),
        ("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía épica", True),
        ("La revolución silenciosa", "Isabel Allende", "Ficción", False),
        ("Sapiens", "Yuval Noah Harari", "No ficción", True),
    ]
    
    print("Cargando datos de ejemplo...\n")
    
    for titulo, autor, genero, leido in libros_ejemplo:
        db.agregar_libro(titulo, autor, genero, leido)
    
    print(f"\n✓ Se agregaron {len(libros_ejemplo)} libros de ejemplo.")
    print(f"Total de libros en la base de datos: {db.contar_libros()}")
    
    db.cerrar()


if __name__ == "__main__":
    respuesta = input("¿Deseas cargar los datos de ejemplo? (s/n): ").strip().lower()
    if respuesta == 's':
        cargar_datos_ejemplo()
        print("\n✓ Datos cargados. Ahora puedes ejecutar main.py para usar la aplicación.")
    else:
        print("Operación cancelada.")
