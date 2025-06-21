from db import conectar_db
from libro import Libro
import mysql.connector

class Autor:
    def __init__(self, id_autor=None, nombre=None, nacionalidad=None, fecha_nacimiento=None):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def guardar(self):
        db = conectar_db()
        cursor = db.cursor()

        if self.id_autor is None:
            sql = "INSERT INTO Autores (nombre, nacionalidad, fecha_nacimiento) VALUES (%s, %s, %s)"
            val = (self.nombre, self.nacionalidad, self.fecha_nacimiento)
            cursor.execute(sql, val)
            self.id_autor = cursor.lastrowid
        else:
            sql = "UPDATE Autores SET nombre=%s, nacionalidad=%s, fecha_nacimiento=%s WHERE id_autor=%s"
            val = (self.nombre, self.nacionalidad, self.fecha_nacimiento, self.id_autor)
            cursor.execute(sql, val)

        db.commit()
        db.close()
        print("Autor guardado correctamente.")

    def buscar_id_autor(self):
        db = conectar_db()
        cursor = db.cursor()
        cursor.execute("SELECT id_autor FROM Autores WHERE nombre = %s", (self.nombre,))
        autor = cursor.fetchone()
        if autor:
            self.id_autor = autor[0]
            return self.id_autor
        db.close()

    def eliminar_autor (self):
        db = conectar_db()
        cursor = db.cursor()
        self.id_autor = self.buscar_id_autor()
        try:
            # verificar si el libro existe en la base de datos
            if self.id_autor is None:
                print ("El libro no tinene un ID válido para eliminar.")
                return
            else:
                cursor.execute("DELETE FROM Autores WHERE id_autor = %s", (self.id_autor,))
                db.commit()
                print ("Autor eliminado correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al eliminar el libreo: {err} ")
        finally:
            db.close()

    def modificar_autor (self):
        db = conectar_db()
        cursor = db.cursor()
        self.id_autor = self.buscar_id_autor()
        nombre_cambiar = input ("Pon el nombre:")    
        nacionalidad_cambiar = input ("Pon la nacionalidad: ")   
        fecha_nacimiento_cambiar = input ("Pon la fecha de nacimiento: ") 
        try:  
            if self.id_autor is None:
                print ("No tiene un ID válido")    
            else:
                cursor.execute("UPDATE Autores SET nombre=%s, nacionalidad=%s, fecha_nacimiento=%s WHERE id_autor=%s", 
                               (nombre_cambiar, nacionalidad_cambiar, fecha_nacimiento_cambiar))
                db.commit()
                print ("Autor actualizado correctamente.")
        except mysql.connector.Error as err:
            print (f"Error al actualizar el autor: {err} ")
        finally:
            db.close()

