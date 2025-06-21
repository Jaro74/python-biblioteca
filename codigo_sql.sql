
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

-- Crear tabla Autores
CREATE TABLE IF NOT EXISTS Autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    nacionalidad VARCHAR(100),
    fecha_nacimiento DATE
);

-- Crear tabla Generos
CREATE TABLE IF NOT EXISTS Generos (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE
);

-- Crear tabla Libros
CREATE TABLE IF NOT EXISTS Libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    id_autor INT,
    id_genero INT,
    anio_publicacion INT,
    isbn VARCHAR(20) UNIQUE,
    disponible BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor) ON DELETE CASCADE, -- pongo ON DELETE CASCADE para poder eliminar
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero) ON DELETE CASCADE
);

--Buscar por Título:
SELECT * FROM Libros
WHERE titulo LIKE '%PalabraClave%';

--Buscar por Autor:
SELECT * FROM Libros
WHERE autor LIKE '%NombreAutor%';

--Buscar por Género
SELECT * FROM Libros
WHERE genero LIKE '%Genero%';

-- Insertar nuevos libros
INSERT INTO Libros (titulo, autor, genero, anio_publicacion, isbn, disponible)
VALUES ('El Quijote', 'Miguel de Cervantes', 'Ficción', 1605, '978-1234567890', TRUE);

--Actualizar libros
UPDATE Libros
SET titulo = 'Nuevo Título', autor = 'Nuevo Autor', genero = 'Nuevo Género'
WHERE id_libro = 1;

-- Eliminar libros
DELETE FROM Libros
WHERE id_libro = 1;

-- eliminar de disponible
UPDATE Libros
SET disponible = FALSE
WHERE id_libro = 1;