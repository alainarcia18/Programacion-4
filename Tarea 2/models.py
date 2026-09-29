# -*- coding: utf-8 -*-
"""
Módulo de modelos para la base de datos de biblioteca.
Define la estructura del objeto Libro.
"""


class Libro:
    """Representa un libro en la biblioteca personal."""
    
    def __init__(self, libro_id=None, titulo="", autor="", genero="", leido=False):
        """
        Inicializa un objeto Libro.
        
        Args:
            libro_id (int): ID único del libro
            titulo (str): Título del libro
            autor (str): Autor del libro
            genero (str): Género del libro
            leido (bool): Estado de lectura (True = leído, False = no leído)
        """
        self.id = libro_id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.leido = leido
    
    def __str__(self):
        """Representación en string del libro."""
        estado = "✓ Leído" if self.leido else "✗ No leído"
        return f"[{self.id}] {self.titulo} | {self.autor} | {self.genero} | {estado}"
    
    def __repr__(self):
        """Representación para debugging."""
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', genero='{self.genero}', leido={self.leido})"
    
    def marcar_leido(self):
        """Marca el libro como leído."""
        self.leido = True
    
    def marcar_no_leido(self):
        """Marca el libro como no leído."""
        self.leido = False
