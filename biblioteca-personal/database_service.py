"""
Servicio de base de datos que proporciona operaciones CRUD
para la gestión de libros en la biblioteca personal.
Maneja todas las excepciones relacionadas con la base de datos.
"""

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from models import Libro, get_session
from typing import List, Optional, Tuple


class DatabaseService:
    """Servicio para manejar todas las operaciones con la base de datos"""
    
    @staticmethod
    def agregar_libro(titulo: str, autor: str, genero: str, leido: bool = False) -> Tuple[bool, str]:
        """
        Agrega un nuevo libro a la biblioteca.
        
        Args:
            titulo: Título del libro
            autor: Autor del libro
            genero: Género del libro
            leido: Estado de lectura (por defecto False)
            
        Returns:
            Tupla (éxito, mensaje)
        """
        session = get_session()
        try:
            # Validar que los campos no estén vacíos
            if not titulo.strip() or not autor.strip() or not genero.strip():
                return False, "Error: Los campos no pueden estar vacíos"
            
            nuevo_libro = Libro(
                titulo=titulo.strip(),
                autor=autor.strip(),
                genero=genero.strip(),
                leido=leido
            )
            
            session.add(nuevo_libro)
            session.commit()
            return True, f"✓ Libro '{titulo}' agregado correctamente (ID: {nuevo_libro.id})"
            
        except IntegrityError as e:
            session.rollback()
            return False, f"Error de integridad en la base de datos: {str(e)}"
        except SQLAlchemyError as e:
            session.rollback()
            return False, f"Error en la base de datos: {str(e)}"
        except Exception as e:
            session.rollback()
            return False, f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def obtener_todos_libros() -> Tuple[bool, List[Libro], str]:
        """
        Obtiene todos los libros de la base de datos.
        
        Returns:
            Tupla (éxito, lista_de_libros, mensaje)
        """
        session = get_session()
        try:
            libros = session.query(Libro).order_by(Libro.id).all()
            return True, libros, f"Se encontraron {len(libros)} libro(s)"
        except SQLAlchemyError as e:
            return False, [], f"Error en la base de datos: {str(e)}"
        except Exception as e:
            return False, [], f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def buscar_libros(criterio: str, tipo_busqueda: str = 'titulo') -> Tuple[bool, List[Libro], str]:
        """
        Busca libros según un criterio específico.
        
        Args:
            criterio: Texto a buscar
            tipo_busqueda: 'titulo', 'autor' o 'genero'
            
        Returns:
            Tupla (éxito, lista_de_libros, mensaje)
        """
        session = get_session()
        try:
            if not criterio.strip():
                return False, [], "Error: El criterio de búsqueda no puede estar vacío"
            
            criterio_lower = f"%{criterio.lower()}%"
            
            if tipo_busqueda == 'titulo':
                libros = session.query(Libro).filter(
                    Libro.titulo.ilike(criterio_lower)
                ).all()
            elif tipo_busqueda == 'autor':
                libros = session.query(Libro).filter(
                    Libro.autor.ilike(criterio_lower)
                ).all()
            elif tipo_busqueda == 'genero':
                libros = session.query(Libro).filter(
                    Libro.genero.ilike(criterio_lower)
                ).all()
            else:
                return False, [], "Tipo de búsqueda no válido"
            
            if libros:
                return True, libros, f"Se encontraron {len(libros)} resultado(s)"
            else:
                return True, [], f"No se encontraron libros con {tipo_busqueda} '{criterio}'"
                
        except SQLAlchemyError as e:
            return False, [], f"Error en la base de datos: {str(e)}"
        except Exception as e:
            return False, [], f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def obtener_libro_por_id(libro_id: int) -> Tuple[bool, Optional[Libro], str]:
        """
        Obtiene un libro específico por su ID.
        
        Args:
            libro_id: ID del libro a buscar
            
        Returns:
            Tupla (éxito, libro, mensaje)
        """
        session = get_session()
        try:
            libro = session.query(Libro).filter(Libro.id == libro_id).first()
            if libro:
                return True, libro, f"Libro encontrado"
            else:
                return False, None, f"No se encontró libro con ID {libro_id}"
        except SQLAlchemyError as e:
            return False, None, f"Error en la base de datos: {str(e)}"
        except Exception as e:
            return False, None, f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def actualizar_libro(libro_id: int, **kwargs) -> Tuple[bool, str]:
        """
        Actualiza los datos de un libro.
        
        Args:
            libro_id: ID del libro a actualizar
            **kwargs: Campos a actualizar (titulo, autor, genero, leido)
            
        Returns:
            Tupla (éxito, mensaje)
        """
        session = get_session()
        try:
            libro = session.query(Libro).filter(Libro.id == libro_id).first()
            
            if not libro:
                return False, f"No se encontró libro con ID {libro_id}"
            
            # Campos permitidos para actualizar
            campos_permitidos = {'titulo', 'autor', 'genero', 'leido'}
            
            for campo, valor in kwargs.items():
                if campo in campos_permitidos:
                    if campo in ['titulo', 'autor', 'genero']:
                        if not valor.strip():
                            return False, f"Error: El campo '{campo}' no puede estar vacío"
                        setattr(libro, campo, valor.strip())
                    else:
                        setattr(libro, campo, valor)
            
            session.commit()
            return True, f"✓ Libro con ID {libro_id} actualizado correctamente"
            
        except IntegrityError as e:
            session.rollback()
            return False, f"Error de integridad en la base de datos: {str(e)}"
        except SQLAlchemyError as e:
            session.rollback()
            return False, f"Error en la base de datos: {str(e)}"
        except Exception as e:
            session.rollback()
            return False, f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def eliminar_libro(libro_id: int) -> Tuple[bool, str]:
        """
        Elimina un libro de la base de datos.
        
        Args:
            libro_id: ID del libro a eliminar
            
        Returns:
            Tupla (éxito, mensaje)
        """
        session = get_session()
        try:
            libro = session.query(Libro).filter(Libro.id == libro_id).first()
            
            if not libro:
                return False, f"No se encontró libro con ID {libro_id}"
            
            titulo_libro = libro.titulo
            session.delete(libro)
            session.commit()
            return True, f"✓ Libro '{titulo_libro}' eliminado correctamente"
            
        except SQLAlchemyError as e:
            session.rollback()
            return False, f"Error en la base de datos: {str(e)}"
        except Exception as e:
            session.rollback()
            return False, f"Error inesperado: {str(e)}"
        finally:
            session.close()
    
    @staticmethod
    def obtener_estadisticas() -> dict:
        """
        Obtiene estadísticas sobre la biblioteca.
        
        Returns:
            Diccionario con estadísticas
        """
        session = get_session()
        try:
            total_libros = session.query(Libro).count()
            libros_leidos = session.query(Libro).filter(Libro.leido == True).count()
            libros_no_leidos = total_libros - libros_leidos
            
            # Género más común
            generos = session.query(Libro.genero).all()
            genero_popular = None
            if generos:
                from collections import Counter
                contador = Counter([g[0] for g in generos])
                genero_popular = contador.most_common(1)[0][0]
            
            return {
                'total_libros': total_libros,
                'libros_leidos': libros_leidos,
                'libros_no_leidos': libros_no_leidos,
                'porcentaje_leido': round((libros_leidos / total_libros * 100) if total_libros > 0 else 0, 2),
                'genero_popular': genero_popular
            }
        except Exception as e:
            print(f"Error al obtener estadísticas: {str(e)}")
            return {}
        finally:
            session.close()
