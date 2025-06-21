from db import conectar_db
from libro import Libro
import mysql.connector


# clase Biblioteca
class Biblioteca:
    # creo @staticmethod para que no sea necesario instanciar la clase para usar el método
    @staticmethod
    def buscar_libros_por_autor(nombre_autor):
        db = conectar_db()
        cursor = db.cursor()

        # sql = """
        # SELECT Libros.id_libro, Libros.titulo, Autores.nombre, Generos.nombre, Libros.anio_publicacion, Libros.isbn, Libros.disponible
        # FROM Libros
        # JOIN Autores ON Libros.id_autor = Autores.id_autor
        # JOIN Generos ON Libros.id_genero = Generos.id_genero
        # WHERE Autores.nombre LIKE %s
        # """
        # cursor.execute(sql, ('%' + nombre_autor + '%',))
        cursor.execute("""
        SELECT Libros.id_libro, Libros.titulo, Autores.nombre, Generos.nombre, Libros.anio_publicacion, Libros.isbn, libros.disponible
        FROM Libros
        JOIN Autores ON Libros.id_autor = Autores.id_autor
        JOIN Generos ON Libros.id_genero = Generos.id_genero
        WHERE Autores.nombre LIKE %s
        """, ('%' + nombre_autor + '%',))
        libros = cursor.fetchall()

        # Si se encontraron libros, los muestro
        if libros:
            for libro in libros:
                estado = "Disponible" if libro[6] else "No Disponible"
                print(f"{libro[1]} - {libro[2]} ({libro[4]}) | {libro[3]} | ISBN: {libro[5]} | {estado}")
        else:
            print("No se encontraron libros para este autor.")

        db.close()

    @staticmethod
    def obtener_id_libro(titulo):
        db = conectar_db()
        cursor = db.cursor()    
        try:
            cursor.execute("SELECT id_libro FROM libros WHERE titulo = %s",(titulo,))
            libro_data = cursor.fetchone()

            if libro_data:
                return libro_data [0]
            else:
                return None
        except mysql.connector.Error as err:
            print (f"Error al obtener el libro: {err}")
            return None
        finally:
            db.close()

    @staticmethod
    def buscar_libros_por_genero (nombre_genero):
        try:
            db = conectar_db()
            cursor = db.cursor()
            cursor.execute(""""
            SELECT Libros.id_libro, Libros.titulo, Autores.nombre, Generos.nombre, Libros.anio_publicacion, Libros.isbn, libros.disponible
            FROM Libros
            JOIN Autores ON Libros.id_autor = Autores.id_autor
            JOIN Generos ON Libros.id_genero = Generos.id_genero
            WHERE Generos.nombre LIKE %s
            """, ("%" + nombre_genero + "%",))
            libros = cursor.fetchall()
            if libros:
                for libro in libros:
                    estado = "Disponible" if libro[6] else "No Disponible"
                    print(f"{libro[1]} - {libro[2]} ({libro[4]}) | {libro[3]} | ISBN: {libro[5]} | {estado}")
                else:
                    print("No se encontraron libros para este genero.")
        except mysql.connector.Error as err:
            print (f"Error al obtner los libres: {err}")
        finally:
            db.close()


                    
    @staticmethod
    def buscar_id (nombre_buscar, tabla_buscar):
        db = conectar_db()
        cursor = db.cursor()
        try:
            cursor.execute (f"SELECT id_autor FROM {tabla_buscar} WHERE nombre =%s", (nombre_buscar,))   
            busqueda = cursor.fetchone()
            if busqueda:
                return busqueda [0]
        except mysql.connector.Error as err:
            print (f" Error al obtener el dato: {err}")
        finally:
            db.close()


    @staticmethod
    def eliminar_objeto (id_buscar, tabla_buscar):
        db = conectar_db()
        cursor = db.cursor()
        id_buscar = Biblioteca.buscar_id(id_buscar, tabla_buscar)
        try:
            if id_buscar is None:
                print ("El objeto no tiene un ID válido para eliminar.")
                return
            else:
                cursor.execute(f"DELETE FROM {tabla_buscar} WHERE {id_buscar} = %s", (id_buscar,))   
                db.commit()
                print (f" {tabla_buscar} eliminada correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al eliminar el objeto: {err}")
        finally:
            db.close()   