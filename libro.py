from db import conectar_db
from autor_model import Autor
from genero import Genero
from biblioteca import Biblioteca
import mysql.connector

# Clase libro
class Libro:
    def __init__(self, id_libro=None, titulo=None, autor=None, genero=None, anio_publicacion=None, isbn=None, disponible=True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.isbn = isbn
        self.disponible = disponible

    # Función para guardar un libro en la base de datos
    def guardar(self):
        db = conectar_db()
        cursor = db.cursor()
        # Si el autor no tiene ID, se guarda en la base de datos
        if self.id_libro is None:
            sql = "INSERT INTO Libros (titulo, id_autor, id_genero, anio_publicacion, isbn, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (self.titulo, self.autor.id_autor, self.genero.id_genero, self.anio_publicacion, self.isbn, self.disponible)
            cursor.execute(sql, val)
        #     cursor.execute("""INSERT INTO LIBROS (titulo, id_autor, id_genero, anio_publicacion, isbn, disponible)
        #                    VALUES (%s, %s, %s, %s, %s, %s)""", (self.titulo, self.autor.id_autor, self.genero.id_genero, self.anio_publicacion, self.isbn, self.disponible))
            self.id_libro = cursor.lastrowid # Obtiene el ID del libro recien insertado
        # Si el autor ya tiene ID, se actualiza en la base de datos    
        else:
            sql = "UPDATE Libros SET titulo=%s, id_autor=%s, id_genero=%s, anio_publicacion=%s, isbn=%s, disponible=%s WHERE id_libro=%s"
            val = (self.titulo, self.autor.id_autor, self.genero.id_genero, self.anio_publicacion, self.isbn, self.disponible, self.id_libro)
            cursor.execute(sql, val)
        #     cursor.execute("""UPDATE Liboros SET titulo=%s, id_autor=%s, id_genero=%s, anio_publicacion=%s, isbn=%s, disponible=%s 
        #                    WHERE id_libro=%s""",(self.titulo, self.autor.id_autor, self.genero.id_genero, self.anio_publicacion, self.isbn, self.disponible, self.id_libro))
        # cursor.execute(sql, val)
        # cursor.execute("""INSERT INTO LIBROS (titulo, id_autor, id_genero, anio_publicacion, isbn, disponible)
        #                    VALUES (%s, %s, %s, %s, %s, %s)""", (self.titulo, self.autor.id_autor, self.genero.id_genero, self.anio_publicacion, self.isbn, self.disponible))
            self.id_libro = cursor.lastrowid # Obtiene el ID del libro recien insertado
        db.commit()
        db.close()
        print("Libro guardado correctamente.")

    def buscar_id_libro(self):
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_libro FROM Libros WHERE titulo = %s",(self.titulo,))
        libro = cursor.fetchone() # fetchone () recupera la primera fila de un resultado de consulta
        if libro:
            self.id_libro = libro[0]
            return self.id_libro
        db.close()


    # Función para marcar un libro como no disponible
    def marcar_no_disponible(self):
        # Verificar si el id_libro es válido antes de intentar actualizar
        # print(self.id_libro)
        self.id_libro = self.buscar_id_libro()
        if self.id_libro is None:
            print("El libro no tiene un ID válido para actualizar.")
            return

        db = conectar_db()  # Establecer la conexión con la base de datos
        cursor = db.cursor()

        try:
            # Ejecutar la consulta para marcar el libro como no disponible
            cursor.execute("UPDATE Libros SET disponible = 0 WHERE id_libro = %s", (self.id_libro,))

            # Confirmar los cambios en la base de datos
            db.commit()

            # Verificar si se actualizó algún libro
            if cursor.rowcount == 0:
                print(f"No se encontró un libro con ID {self.id_libro}.")
            else:
                print(f"Libro '{self.titulo}' marcado como no disponible.")
        except mysql.connector.Error as err:
            # Capturar cualquier error de MySQL y mostrarlo
            print(f"Error al actualizar el libro: {err}")
        finally:
            # Cerrar la conexión a la base de datos
            db.close()

     # Función para marcar un libro como  disponible
    def marcar_disponible(self):
        # Verificar si el id_libro es válido antes de intentar actualizar
        # print(self.id_libro)
        self.id_libro = self.buscar_id_libro()
        if self.id_libro is None:
            print("El libro no tiene un ID válido para actualizar.")
            return

        db = conectar_db()  # Establecer la conexión con la base de datos
        cursor = db.cursor()

        try:
            # Ejecutar la consulta para marcar el libro como no disponible
            cursor.execute("UPDATE Libros SET disponible = 1 WHERE id_libro = %s", (self.id_libro,))

            # Confirmar los cambios en la base de datos
            db.commit()

            # Verificar si se actualizó algún libro
            if cursor.rowcount == 0:
                print(f"No se encontró un libro con ID {self.id_libro}.")
            else:
                print(f"Libro '{self.titulo}' marcado como no disponible.")
        except mysql.connector.Error as err:
            # Capturar cualquier error de MySQL y mostrarlo
            print(f"Error al actualizar el libro: {err}")
        finally:
            # Cerrar la conexión a la base de datos
            db.close()

    def eliminar_libro (self):
        db = conectar_db()
        cursor = db.cursor()
        self.id_libro = self.buscar_id_libro()
        try:
            # verificar si el libro existe en la base de datos
            if self.id_libro is None:
                print ("El libro no tinene un ID válido para eliminar.")
                return
            else:
                cursor.execute("DELETE FROM libros WHERE id_libro = %S", (self.id_libro,))
                db.commit()
                print ("Libro eliminado correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al eliminar el libreo: {err} ")    
        finally:
            db.close()

    def modificar_libro (self):
        db = conectar_db()
        cursor = db.cursor()
        self.id_autor = self.buscar_id_libro()
        titulo_cambiar = input ("Pon el titulo:")    
        anio_publicacion_cambiar = input ("Pon el añoi de publicación: ")   
        isbn_cambiar = input ("Pon el ISBN: ") 
        id_autor_cambiar = input (" pon el ID del autor")
        id_genero_cambiar = input (" pon el ID del genero")
        if Biblioteca.buscar_id(id_autor_cambiar, "Autores"):
            return
        try:  
            if Biblioteca.buscar_id(id_autor_cambiar, "Autores") or Biblioteca.buscar_id(id_genero_cambiar) is None:
                print ("No tiene un ID válido")    
            else:
                cursor.execute("UPDATE Libros SET titulo=%s, id_autor=%s, id_genero=%s, anio_publicacion=%s, isbn=%s, disponible=%s WHERE id_libro=%s", 
                               (titulo_cambiar, id_autor_cambiar, id_autor_cambiar, anio_publicacion_cambiar, isbn_cambiar ))
                db.commit()
                print ("Autor actualizado correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al actualizar el autor: {err} ")
        finally:
            db.close()        

        