# -*- coding: utf-8 -*-
"""
Módulo de aplicación con el menú interactivo.
Gestiona la interfaz de usuario en consola.
"""

from database import BaseDatos


class BibliotecaApp:
    """Aplicación de gestión de biblioteca personal."""
    
    def __init__(self):
        """Inicializa la aplicación y conecta a la base de datos."""
        self.db = BaseDatos("biblioteca.db")
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu(self):
        """Muestra el menú principal de la aplicación."""
        print("\n" + "="*50)
        print(" "*10 + "BIBLIOTECA PERSONAL")
        print("="*50)
        print("1. Agregar nuevo libro")
        print("2. Ver todos los libros")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Ver estadísticas")
        print("7. Salir")
        print("="*50)
    
    def agregar_libro(self):
        """Opción para agregar un nuevo libro."""
        print("\n--- AGREGAR NUEVO LIBRO ---")
        try:
            titulo = input("Título del libro: ").strip()
            if not titulo:
                print("✗ El título no puede estar vacío.")
                return
            
            autor = input("Autor: ").strip()
            if not autor:
                print("✗ El autor no puede estar vacío.")
                return
            
            genero = input("Género: ").strip()
            if not genero:
                print("✗ El género no puede estar vacío.")
                return
            
            while True:
                leido_input = input("¿Ya lo has leído? (s/n): ").strip().lower()
                if leido_input in ['s', 'n']:
                    leido = leido_input == 's'
                    break
                print("✗ Por favor, ingresa 's' o 'n'.")
            
            self.db.agregar_libro(titulo, autor, genero, leido)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def ver_todos_libros(self):
        """Opción para ver todos los libros."""
        print("\n--- LISTA DE LIBROS ---")
        libros = self.db.obtener_todos_libros()
        
        if not libros:
            print("No hay libros registrados en la biblioteca.")
            return
        
        print(f"\nTotal de libros: {len(libros)}\n")
        for libro in libros:
            print(libro)
    
    def buscar_libro(self):
        """Opción para buscar libros."""
        print("\n--- BUSCAR LIBRO ---")
        print("Buscar por:")
        print("1. Título")
        print("2. Autor")
        print("3. Género")
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            criterios = {'1': 'titulo', '2': 'autor', '3': 'genero'}
            if opcion not in criterios:
                print("✗ Opción inválida.")
                return
            
            criterio = criterios[opcion]
            valor = input(f"Ingresa el {criterio} a buscar: ").strip()
            
            if not valor:
                print("✗ El valor de búsqueda no puede estar vacío.")
                return
            
            resultados = self.db.buscar_libros(criterio, valor)
            
            if not resultados:
                print(f"✗ No se encontraron libros con ese {criterio}.")
                return
            
            print(f"\nResultados de búsqueda: {len(resultados)} libro(s)\n")
            for libro in resultados:
                print(libro)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def actualizar_libro(self):
        """Opción para actualizar información de un libro."""
        print("\n--- ACTUALIZAR LIBRO ---")
        try:
            self.ver_todos_libros()
            
            libro_id = input("\nIngresa el ID del libro a actualizar: ").strip()
            if not libro_id.isdigit():
                print("✗ ID inválido.")
                return
            
            libro_id = int(libro_id)
            libro = self.db.obtener_libro_por_id(libro_id)
            
            if not libro:
                print(f"✗ No se encontró el libro con ID {libro_id}")
                return
            
            print(f"\nLibro actual: {libro}")
            print("\nDeja en blanco para mantener el valor actual.\n")
            
            titulo = input(f"Nuevo título ({libro.titulo}): ").strip() or None
            autor = input(f"Nuevo autor ({libro.autor}): ").strip() or None
            genero = input(f"Nuevo género ({libro.genero}): ").strip() or None
            
            leido = None
            while True:
                cambiar_leido = input("¿Cambiar estado de lectura? (s/n/x para no cambiar): ").strip().lower()
                if cambiar_leido == 'x':
                    break
                elif cambiar_leido in ['s', 'n']:
                    leido = cambiar_leido == 's'
                    break
                print("✗ Por favor, ingresa 's', 'n' o 'x'.")
            
            self.db.actualizar_libro(libro_id, titulo, autor, genero, leido)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def eliminar_libro(self):
        """Opción para eliminar un libro."""
        print("\n--- ELIMINAR LIBRO ---")
        try:
            self.ver_todos_libros()
            
            libro_id = input("\nIngresa el ID del libro a eliminar: ").strip()
            if not libro_id.isdigit():
                print("✗ ID inválido.")
                return
            
            libro_id = int(libro_id)
            confirmacion = input("¿Estás seguro de que deseas eliminar este libro? (s/n): ").strip().lower()
            
            if confirmacion == 's':
                self.db.eliminar_libro(libro_id)
            else:
                print("Eliminación cancelada.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def ver_estadisticas(self):
        """Opción para ver estadísticas de la biblioteca."""
        print("\n--- ESTADÍSTICAS ---")
        total = self.db.contar_libros()
        leidos = self.db.contar_libros_leidos()
        no_leidos = total - leidos
        
        print(f"Total de libros: {total}")
        print(f"Libros leídos: {leidos}")
        print(f"Libros no leídos: {no_leidos}")
        
        if total > 0:
            porcentaje = (leidos / total) * 100
            print(f"Porcentaje de libros leídos: {porcentaje:.1f}%")
    
    def ejecutar(self):
        """Ejecuta el ciclo principal de la aplicación."""
        try:
            while True:
                self.mostrar_menu()
                opcion = input("Selecciona una opción (1-7): ").strip()
                
                if opcion == '1':
                    self.agregar_libro()
                elif opcion == '2':
                    self.ver_todos_libros()
                elif opcion == '3':
                    self.buscar_libro()
                elif opcion == '4':
                    self.actualizar_libro()
                elif opcion == '5':
                    self.eliminar_libro()
                elif opcion == '6':
                    self.ver_estadisticas()
                elif opcion == '7':
                    print("\n✓ ¡Gracias por usar la Biblioteca Personal!")
                    self.db.cerrar()
                    break
                else:
                    print("✗ Opción inválida. Por favor, selecciona una opción válida.")
                
                input("\nPresiona Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\n✓ Aplicación interrumpida. ¡Hasta luego!")
            self.db.cerrar()
        except Exception as e:
            print(f"\n✗ Error inesperado: {e}")
            self.db.cerrar()
