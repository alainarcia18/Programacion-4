"""
Modelos de SQLAlchemy para la aplicación de biblioteca personal
Define la estructura de la tabla 'libros' con sus relaciones y validaciones
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL, SQLALCHEMY_CONFIG

# Base para todos los modelos
Base = declarative_base()


class Libro(Base):
    """
    Modelo que representa un libro en la biblioteca personal.
    
    Atributos:
        id: Identificador único del libro
        titulo: Título del libro
        autor: Nombre del autor
        genero: Género literario del libro
        leido: Estado de lectura (True = leído, False = no leído)
        fecha_creacion: Fecha de creación del registro
        fecha_actualizacion: Fecha de última actualización
    """
    
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False, index=True)
    autor = Column(String(255), nullable=False, index=True)
    genero = Column(String(100), nullable=False)
    leido = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    
    def __repr__(self):
        """Representación en string del objeto Libro"""
        return f"<Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', genero='{self.genero}', leido={self.leido})>"
    
    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'leido': self.leido,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            'fecha_actualizacion': self.fecha_actualizacion.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def estado_lectura(self):
        """Retorna el estado de lectura en formato legible"""
        return "Leído" if self.leido else "No leído"


# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, **SQLALCHEMY_CONFIG)

# Crear la sesión
Session = sessionmaker(bind=engine)


def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas.
    Debe ejecutarse una sola vez.
    """
    try:
        Base.metadata.create_all(engine)
        print("✓ Base de datos inicializada correctamente")
        return True
    except Exception as e:
        print(f"✗ Error al inicializar la base de datos: {e}")
        return False


def get_session():
    """
    Obtiene una nueva sesión de SQLAlchemy.
    
    Returns:
        Session: Una sesión de SQLAlchemy para realizar operaciones con la BD
    """
    return Session()
