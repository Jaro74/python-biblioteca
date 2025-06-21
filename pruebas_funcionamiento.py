from autor_model import Autor
from genero import Genero
from libro import Libro
from biblioteca import Biblioteca

def main():
    pass

#Crear Autor y Género
# autor = Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano", fecha_nacimiento="1927-03-06")
# autor.guardar()

# genero = Genero(nombre="Realismo Mágico")
# genero.guardar()

# # Crear y Guardar Libro
# libro = Libro(titulo="Cien Años de Soledad", autor=autor, genero=genero, anio_publicacion=1967, isbn="978-8437604947")
# libro.guardar()

# autor = Autor(nombre="Camilo José Cela", nacionalidad= "Española", fecha_nacimiento="1916-03-11")
# autor.guardar()

# genero = Genero(nombre="Postguerra española")
# genero.guardar()

# # Crear y Guardar Libro
# libro = Libro(titulo="La familia de Pascual Duarte", autor=autor, genero=genero, anio_publicacion= 1942, isbn="978-8466349314")
# libro.guardar()

# autor = Autor(nombre="Richard Bach", nacionalidad= "Estadounidense", fecha_nacimiento="1936-06-26")
# autor.guardar()

# genero = Genero(nombre="Fabula")
# genero.guardar()

# # Crear y Guardar Libro
# libro = Libro(titulo="Juan Salvador Gaviota", autor=autor, genero=genero, anio_publicacion= 1942, isbn="978-8416076444")
# libro.guardar()
# genero = Genero(nombre="Informatica")
# genero.guardar()

# Crear y guardar libro para que aparezca el id en la base de datos
autor = Autor(id_autor=1)  # Supongamos que el autor con ID 1 ya existe
genero = Genero(id_genero=8)  # Supongamos que el género con ID 8 ya existe
libro1 = Libro(titulo="Python Avanzado", autor=autor, genero=genero, anio_publicacion=2024, isbn="1234567890")
# libro1.guardar()

autor = Autor(id_autor=1)  # Supongamos que el autor con ID 1 ya existe
genero = Genero(id_genero=8)  # Supongamos que el género con ID 8 ya existe
libro2 = Libro(titulo="Java Avanzado", autor=autor, genero=genero, anio_publicacion=2024, isbn="1234567890-464")
# libro2.guardar()

# Buscar libros por autor
nombre_autor = "Gabriel García Márquez"
biblio = Biblioteca()
print("\n Buscando libros de 'Gabriel García Márquez':")
biblio.buscar_libros_por_autor(nombre_autor)

# Marcar como no disponible
print("\n Marcando libro como no disponible:")
libro2.marcar_no_disponible()

# Verificar estado actualizado
print("\n Verificar estado actualizado:")
Biblioteca.buscar_libros_por_autor("Gabriel García Márquez")
