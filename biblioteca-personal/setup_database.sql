-- ============================================================
-- Script de Configuración de Base de Datos - Biblioteca Personal
-- MariaDB 10.5+
-- ============================================================

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca_personal
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos
USE biblioteca_personal;

-- Crear tabla de libros
CREATE TABLE IF NOT EXISTS libros (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único del libro',
    titulo VARCHAR(255) NOT NULL COMMENT 'Título del libro',
    autor VARCHAR(255) NOT NULL COMMENT 'Nombre del autor',
    genero VARCHAR(100) NOT NULL COMMENT 'Género literario',
    leido BOOLEAN DEFAULT FALSE COMMENT 'Estado de lectura',
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de creación',
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Fecha de última actualización',
    
    -- Índices para mejora de rendimiento
    INDEX idx_titulo (titulo),
    INDEX idx_autor (autor),
    INDEX idx_genero (genero),
    INDEX idx_leido (leido),
    INDEX idx_fecha_creacion (fecha_creacion)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='Tabla principal de libros de la biblioteca personal';

-- ============================================================
-- Datos de ejemplo (opcional)
-- ============================================================

-- INSERT INTO libros (titulo, autor, genero, leido) VALUES
-- ('El Quijote', 'Miguel de Cervantes', 'Novela', TRUE),
-- ('Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', TRUE),
-- ('El Principito', 'Antoine de Saint-Exupéry', 'Novela infantil', TRUE),
-- ('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', TRUE),
-- ('1984', 'George Orwell', 'Distopía', FALSE),
-- ('Orgullo y prejuicio', 'Jane Austen', 'Novela romántica', FALSE),
-- ('El Conde de Montecristo', 'Alejandro Dumas', 'Novela de aventura', FALSE),
-- ('Crimen y castigo', 'Fiódor Dostoievski', 'Novela psicológica', FALSE);

-- ============================================================
-- Vistas útiles
-- ============================================================

-- Vista: Resumen de estadísticas
CREATE OR REPLACE VIEW vista_estadisticas AS
SELECT 
    COUNT(*) as total_libros,
    SUM(CASE WHEN leido = 1 THEN 1 ELSE 0 END) as libros_leidos,
    SUM(CASE WHEN leido = 0 THEN 1 ELSE 0 END) as libros_no_leidos,
    ROUND(SUM(CASE WHEN leido = 1 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) as porcentaje_lectura
FROM libros;

-- Vista: Libros por género
CREATE OR REPLACE VIEW vista_libros_por_genero AS
SELECT 
    genero,
    COUNT(*) as cantidad,
    SUM(CASE WHEN leido = 1 THEN 1 ELSE 0 END) as leidos,
    SUM(CASE WHEN leido = 0 THEN 1 ELSE 0 END) as no_leidos
FROM libros
GROUP BY genero
ORDER BY cantidad DESC;

-- Vista: Libros por autor
CREATE OR REPLACE VIEW vista_libros_por_autor AS
SELECT 
    autor,
    COUNT(*) as cantidad,
    SUM(CASE WHEN leido = 1 THEN 1 ELSE 0 END) as leidos,
    SUM(CASE WHEN leido = 0 THEN 1 ELSE 0 END) as no_leidos
FROM libros
GROUP BY autor
ORDER BY cantidad DESC;

-- ============================================================
-- Consultas útiles
-- ============================================================

-- Ver todas las tablas
-- SHOW TABLES;

-- Ver estructura de la tabla
-- DESCRIBE libros;

-- Ver estadísticas
-- SELECT * FROM vista_estadisticas;

-- Ver libros por género
-- SELECT * FROM vista_libros_por_genero;

-- Ver libros por autor
-- SELECT * FROM vista_libros_por_autor;

-- Ver todos los libros ordenados por fecha
-- SELECT * FROM libros ORDER BY fecha_creacion DESC;

-- Ver solo libros leídos
-- SELECT * FROM libros WHERE leido = 1 ORDER BY titulo;

-- Ver solo libros no leídos
-- SELECT * FROM libros WHERE leido = 0 ORDER BY titulo;

-- ============================================================
-- Fin del script
-- ============================================================
