from db import conectar_db
from libro import Libro
import mysql.connector

#clae genero
class Genero:
    def __init__(self, id_genero=None, nombre=None):
        self.id_genero = id_genero
        self.nombre = nombre

    # Función para guardar un genero en la base de datos
    def guardar(self):
        db = conectar_db()
        cursor = db.cursor()

        if self.id_genero is None:
            sql = "INSERT INTO Generos (nombre) VALUES (%s)"
            val = (self.nombre,)
            cursor.execute(sql, val)
            self.id_genero = cursor.lastrowid  #el atributo lastrowid guarda el ID generado automáticamente por la base de datos.
        else:
            sql = "UPDATE Generos SET nombre=%s WHERE id_genero=%s"
            val = (self.nombre, self.id_genero)
            cursor.execute(sql, val)

        db.commit()
        db.close()
        print("Género guardado correctamente.")

    def buscar_id_genero(self):
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_gnero FROM Generos WHERE nombre = %s", (self.nombre,))
        genero = cursor.fetchone()
        if genero:
            self.id_genero = genero[0]
            return self.id_genero
        db.close()

    def eliminar_genero (self):
        db = conectar_db()
        cursor = db.cursor()
        self.id_genero = self.buscar_id_genero()
        try:
            # verificar si el libro existe en la base de datos
            if self.id_genero is None:
                print ("El libro no tinene un ID válido para eliminar.")
                return
            else:
                cursor.execute("DELETE FROM Generos WHERE id_genero = %S", (self.id_genero,))
                db.commit()
                print ("Genero eliminado correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al eliminar el libreo: {err} ")
        finally:
            db.close()
            