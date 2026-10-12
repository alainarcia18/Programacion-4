"""
Aplicación de Biblioteca Personal
Interfaz de usuario basada en menú en consola.
Utiliza SQLAlchemy como ORM y MariaDB como base de datos.
"""

import os
import sys
from models import init_db
from database_service import DatabaseService


class BibliotecaApp:
    """Aplicación principal de la biblioteca personal"""
    
    def __init__(self):
        """Inicializa la aplicación"""
        self.db_service = DatabaseService()
        self.ejecutando = True
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def mostrar_titulo(self):
        """Muestra el título de la aplicación"""
        print("=" * 60)
        print(" " * 15 + "📚 BIBLIOTECA PERSONAL 📚")
        print("=" * 60)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n¿Qué deseas hacer?\n")
        print("1. Agregar nuevo libro")
        print("2. Ver todos los libros")
        print("3. Buscar libro")
        print("4. Actualizar información de un libro")
        print("5. Eliminar un libro")
        print("6. Ver estadísticas")
        print("7. Salir")
        print("\n" + "=" * 60)
    
    def agregar_libro(self):
        """Permite agregar un nuevo libro"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n➕ AGREGAR NUEVO LIBRO\n")
        
        try:
            titulo = input("Título del libro: ").strip()
            if not titulo:
                print("✗ El título no puede estar vacío")
                input("\nPresiona Enter para continuar...")
                return
            
            autor = input("Autor del libro: ").strip()
            if not autor:
                print("✗ El autor no puede estar vacío")
                input("\nPresiona Enter para continuar...")
                return
            
            genero = input("Género del libro: ").strip()
            if not genero:
                print("✗ El género no puede estar vacío")
                input("\nPresiona Enter para continuar...")
                return
            
            leido = input("¿Ya lo has leído? (s/n): ").lower().strip() == 's'
            
            exito, mensaje = self.db_service.agregar_libro(titulo, autor, genero, leido)
            print(f"\n{mensaje}")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def ver_todos_libros(self):
        """Muestra todos los libros registrados"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n📖 LISTADO DE TODOS LOS LIBROS\n")
        
        try:
            exito, libros, mensaje = self.db_service.obtener_todos_libros()
            
            if not exito:
                print(f"✗ {mensaje}")
                input("\nPresiona Enter para continuar...")
                return
            
            if not libros:
                print("No hay libros registrados aún.")
            else:
                print(f"{mensaje}\n")
                print("-" * 60)
                for libro in libros:
                    self._mostrar_libro(libro)
                print("-" * 60)
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def buscar_libro(self):
        """Permite buscar libros"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n🔍 BUSCAR LIBRO\n")
        
        print("¿Por cuál criterio deseas buscar?")
        print("1. Por título")
        print("2. Por autor")
        print("3. Por género")
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            tipos_busqueda = {'1': 'titulo', '2': 'autor', '3': 'genero'}
            
            if opcion not in tipos_busqueda:
                print("✗ Opción no válida")
                input("\nPresiona Enter para continuar...")
                return
            
            criterio = input("\nIngresa el criterio de búsqueda: ").strip()
            
            exito, libros, mensaje = self.db_service.buscar_libros(
                criterio, 
                tipos_busqueda[opcion]
            )
            
            print(f"\n{mensaje}\n")
            
            if exito and libros:
                print("-" * 60)
                for libro in libros:
                    self._mostrar_libro(libro)
                print("-" * 60)
            elif not exito:
                print(f"✗ Error: {mensaje}")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def actualizar_libro(self):
        """Permite actualizar la información de un libro"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n✏️  ACTUALIZAR INFORMACIÓN DE UN LIBRO\n")
        
        try:
            libro_id = input("Ingresa el ID del libro a actualizar: ").strip()
            
            try:
                libro_id = int(libro_id)
            except ValueError:
                print("✗ El ID debe ser un número")
                input("\nPresiona Enter para continuar...")
                return
            
            exito, libro, mensaje = self.db_service.obtener_libro_por_id(libro_id)
            
            if not exito:
                print(f"✗ {mensaje}")
                input("\nPresiona Enter para continuar...")
                return
            
            print(f"\nLibro actual:")
            self._mostrar_libro(libro)
            
            print("\n¿Qué deseas actualizar?")
            print("1. Título")
            print("2. Autor")
            print("3. Género")
            print("4. Estado de lectura")
            print("5. Cancelar")
            
            opcion = input("\nSelecciona una opción (1-5): ").strip()
            
            if opcion == '5':
                print("Operación cancelada")
                input("\nPresiona Enter para continuar...")
                return
            
            actualizaciones = {}
            
            if opcion == '1':
                nuevo_valor = input("Nuevo título: ").strip()
                if nuevo_valor:
                    actualizaciones['titulo'] = nuevo_valor
            elif opcion == '2':
                nuevo_valor = input("Nuevo autor: ").strip()
                if nuevo_valor:
                    actualizaciones['autor'] = nuevo_valor
            elif opcion == '3':
                nuevo_valor = input("Nuevo género: ").strip()
                if nuevo_valor:
                    actualizaciones['genero'] = nuevo_valor
            elif opcion == '4':
                nuevo_valor = input("¿Está leído? (s/n): ").lower().strip() == 's'
                actualizaciones['leido'] = nuevo_valor
            else:
                print("✗ Opción no válida")
                input("\nPresiona Enter para continuar...")
                return
            
            if actualizaciones:
                exito, mensaje = self.db_service.actualizar_libro(libro_id, **actualizaciones)
                print(f"\n{mensaje}")
            else:
                print("No se ingresó ningún valor para actualizar")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def eliminar_libro(self):
        """Permite eliminar un libro"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n🗑️  ELIMINAR LIBRO\n")
        
        try:
            libro_id = input("Ingresa el ID del libro a eliminar: ").strip()
            
            try:
                libro_id = int(libro_id)
            except ValueError:
                print("✗ El ID debe ser un número")
                input("\nPresiona Enter para continuar...")
                return
            
            exito, libro, mensaje = self.db_service.obtener_libro_por_id(libro_id)
            
            if not exito:
                print(f"✗ {mensaje}")
                input("\nPresiona Enter para continuar...")
                return
            
            print(f"\nLibro a eliminar:")
            self._mostrar_libro(libro)
            
            confirmacion = input("\n¿Estás seguro de que deseas eliminar este libro? (s/n): ").lower().strip()
            
            if confirmacion == 's':
                exito, mensaje = self.db_service.eliminar_libro(libro_id)
                print(f"\n{mensaje}")
            else:
                print("\nOperación cancelada")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def ver_estadisticas(self):
        """Muestra estadísticas de la biblioteca"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n📊 ESTADÍSTICAS DE LA BIBLIOTECA\n")
        
        try:
            stats = self.db_service.obtener_estadisticas()
            
            if not stats:
                print("No se pudieron obtener las estadísticas")
            else:
                print(f"Total de libros: {stats['total_libros']}")
                print(f"Libros leídos: {stats['libros_leidos']}")
                print(f"Libros no leídos: {stats['libros_no_leidos']}")
                print(f"Porcentaje de lectura: {stats['porcentaje_leido']}%")
                if stats['genero_popular']:
                    print(f"Género más popular: {stats['genero_popular']}")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        input("\nPresiona Enter para continuar...")
    
    def _mostrar_libro(self, libro):
        """Muestra un libro formateado"""
        print(f"ID: {libro.id}")
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Género: {libro.genero}")
        print(f"Estado: {libro.estado_lectura()}")
        print(f"Creado: {libro.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Actualizado: {libro.fecha_actualizacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
    
    def ejecutar(self):
        """Ejecuta el bucle principal de la aplicación"""
        while self.ejecutando:
            self.mostrar_menu_principal()
            
            try:
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
                    self.salir()
                else:
                    print("✗ Opción no válida. Por favor intenta de nuevo.")
                    input("\nPresiona Enter para continuar...")
            
            except KeyboardInterrupt:
                print("\n\n✗ Aplicación interrumpida por el usuario")
                self.ejecutando = False
            except Exception as e:
                print(f"\n✗ Error inesperado: {str(e)}")
                input("\nPresiona Enter para continuar...")
    
    def salir(self):
        """Sale de la aplicación"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\n¡Hasta luego! Gracias por usar Biblioteca Personal 📚\n")
        self.ejecutando = False


def main():
    """Función principal"""
    print("Inicializando Biblioteca Personal...\n")
    
    # Inicializar la base de datos
    if not init_db():
        print("✗ No se pudo inicializar la base de datos")
        print("Verifica que MariaDB esté instalado y en ejecución")
        sys.exit(1)
    
    # Crear y ejecutar la aplicación
    app = BibliotecaApp()
    app.ejecutar()


if __name__ == "__main__":
    main()
