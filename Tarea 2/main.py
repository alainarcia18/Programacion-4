#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación de Biblioteca Personal
Proyecto: Gestión de libros con SQLite y Python
"""

from app import BibliotecaApp


def main():
    """Función principal que inicia la aplicación."""
    app = BibliotecaApp()
    app.ejecutar()


if __name__ == "__main__":
    main()
