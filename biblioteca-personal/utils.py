"""
Utilidades para la aplicación de Biblioteca Personal
Incluye funciones para testing, limpieza y mantenimiento
"""

from models import get_session, Libro, engine, Base
from database_service import DatabaseService
from sqlalchemy import text


class DatabaseUtils:
    """Utilidades para la base de datos"""
    
    @staticmethod
    def recrear_base_datos():
        """
        Recrea la base de datos eliminando todas las tablas y recreándolas.
        ¡ADVERTENCIA: Esto eliminará todos los datos!
        """
        print("⚠️  ADVERTENCIA: Esta operación eliminará TODOS los datos de la base de datos")
        confirmacion = input("¿Estás seguro? Escribe 'SÍ' para continuar: ").strip()
        
        if confirmacion.upper() != 'SÍ':
            print("Operación cancelada")
            return False
        
        try:
            Base.metadata.drop_all(engine)
            print("✓ Tablas eliminadas")
            
            Base.metadata.create_all(engine)
            print("✓ Tablas recreadas")
            
            return True
        except Exception as e:
            print(f"✗ Error al recrear la base de datos: {str(e)}")
            return False
    
    @staticmethod
    def cargar_datos_ejemplo():
        """Carga datos de ejemplo en la base de datos"""
        libros_ejemplo = [
            ("El Quijote", "Miguel de Cervantes", "Novela", True),
            ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", True),
            ("El Principito", "Antoine de Saint-Exupéry", "Novela infantil", True),
            ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", True),
            ("1984", "George Orwell", "Distopía", False),
            ("Orgullo y prejuicio", "Jane Austen", "Novela romántica", False),
            ("El Conde de Montecristo", "Alejandro Dumas", "Novela de aventura", False),
            ("Crimen y castigo", "Fiódor Dostoievski", "Novela psicológica", False),
            ("La metamorfosis", "Franz Kafka", "Novela corta", False),
            ("Don Juan Tenorio", "José Zorrilla", "Drama", False),
        ]
        
        db_service = DatabaseService()
        
        print("\nCargando datos de ejemplo...\n")
        
        for titulo, autor, genero, leido in libros_ejemplo:
            exito, mensaje = db_service.agregar_libro(titulo, autor, genero, leido)
            if exito:
                print(f"✓ {titulo}")
            else:
                print(f"✗ {titulo}: {mensaje}")
        
        print("\n✓ Datos de ejemplo cargados")
    
    @staticmethod
    def limpiar_base_datos():
        """Elimina todos los libros de la base de datos"""
        confirmacion = input("¿Estás seguro de que deseas eliminar TODOS los libros? (s/n): ").lower()
        
        if confirmacion != 's':
            print("Operación cancelada")
            return False
        
        session = get_session()
        try:
            cantidad = session.query(Libro).delete()
            session.commit()
            print(f"✓ {cantidad} libro(s) eliminado(s)")
            return True
        except Exception as e:
            session.rollback()
            print(f"✗ Error: {str(e)}")
            return False
        finally:
            session.close()
    
    @staticmethod
    def mostrar_estadisticas_detalladas():
        """Muestra estadísticas detalladas de la base de datos"""
        session = get_session()
        try:
            print("\n" + "=" * 60)
            print("ESTADÍSTICAS DETALLADAS DE LA BIBLIOTECA")
            print("=" * 60 + "\n")
            
            # Estadísticas generales
            total = session.query(Libro).count()
            leidos = session.query(Libro).filter(Libro.leido == True).count()
            no_leidos = total - leidos
            
            print(f"Total de libros: {total}")
            print(f"Libros leídos: {leidos}")
            print(f"Libros no leídos: {no_leidos}")
            if total > 0:
                print(f"Porcentaje de lectura: {round(leidos / total * 100, 2)}%\n")
            
            # Por género
            print("LIBROS POR GÉNERO:")
            print("-" * 60)
            generos = session.query(Libro.genero).distinct().all()
            for genero_tuple in generos:
                genero = genero_tuple[0]
                cantidad = session.query(Libro).filter(Libro.genero == genero).count()
                leidos_genero = session.query(Libro).filter(
                    Libro.genero == genero,
                    Libro.leido == True
                ).count()
                print(f"{genero:.<30} {cantidad:>3} libros ({leidos_genero} leídos)")
            
            # Por autor (top 10)
            print("\n\nTOP 10 AUTORES CON MÁS LIBROS:")
            print("-" * 60)
            autores = session.query(Libro.autor).distinct().all()
            autores_count = {}
            for autor_tuple in autores:
                autor = autor_tuple[0]
                cantidad = session.query(Libro).filter(Libro.autor == autor).count()
                autores_count[autor] = cantidad
            
            for i, (autor, cantidad) in enumerate(sorted(autores_count.items(), key=lambda x: x[1], reverse=True)[:10], 1):
                print(f"{i:>2}. {autor:.<40} {cantidad:>2} libro(s)")
            
            # Libros más recientes
            print("\n\nÚLTIMOS 5 LIBROS AGREGADOS:")
            print("-" * 60)
            recientes = session.query(Libro).order_by(Libro.fecha_creacion.desc()).limit(5).all()
            for libro in recientes:
                print(f"- {libro.titulo}")
                print(f"  Autor: {libro.autor} | Estado: {libro.estado_lectura()}")
            
            print("\n" + "=" * 60 + "\n")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        finally:
            session.close()
    
    @staticmethod
    def exportar_csv(nombre_archivo='libros.csv'):
        """Exporta todos los libros a un archivo CSV"""
        import csv
        
        session = get_session()
        try:
            libros = session.query(Libro).all()
            
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Título', 'Autor', 'Género', 'Leído', 'Fecha Creación', 'Fecha Actualización']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for libro in libros:
                    writer.writerow({
                        'ID': libro.id,
                        'Título': libro.titulo,
                        'Autor': libro.autor,
                        'Género': libro.genero,
                        'Leído': 'Sí' if libro.leido else 'No',
                        'Fecha Creación': libro.fecha_creacion,
                        'Fecha Actualización': libro.fecha_actualizacion
                    })
            
            print(f"✓ Datos exportados a '{nombre_archivo}'")
            return True
        except Exception as e:
            print(f"✗ Error al exportar: {str(e)}")
            return False
        finally:
            session.close()


def menu_utilidades():
    """Menú de utilidades"""
    while True:
        print("\n" + "=" * 60)
        print("UTILIDADES DE MANTENIMIENTO")
        print("=" * 60)
        print("\n1. Cargar datos de ejemplo")
        print("2. Ver estadísticas detalladas")
        print("3. Limpiar base de datos (eliminar todos los libros)")
        print("4. Recrear base de datos (elimina TODO)")
        print("5. Exportar a CSV")
        print("6. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            DatabaseUtils.cargar_datos_ejemplo()
        elif opcion == '2':
            DatabaseUtils.mostrar_estadisticas_detalladas()
        elif opcion == '3':
            DatabaseUtils.limpiar_base_datos()
        elif opcion == '4':
            DatabaseUtils.recrear_base_datos()
        elif opcion == '5':
            nombre = input("Nombre del archivo (default: libros.csv): ").strip()
            if not nombre:
                nombre = 'libros.csv'
            DatabaseUtils.exportar_csv(nombre)
        elif opcion == '6':
            break
        else:
            print("✗ Opción no válida")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    menu_utilidades()
