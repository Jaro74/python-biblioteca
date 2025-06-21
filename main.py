from autor_model import Autor
from genero import Genero
from libro import Libro
from biblioteca import Biblioteca

def main():
    print ("+"*50)
    print (""""
            1. Crear Autor
            2. Crear género
            3. Crear libro
            4. Buscar libros por autor
            5. Buscar libros por genero
            6. Marcar libro como no disponible
            7. Marcar libro como disponible  
            8. Modificar
            9. Eliminar
            10. Salir     
        """)
    print ("+"*50)

    opcion = input("Selecione una opción: ")
    if opcion == "1":
        nombre_autor = input("Ingrese el nombre del autor: ")
        nacionalidad = input("Ingrese la nacionalidad del autor: ")
        fecha_nacimiento = input ("Ingrese la fecha de nacimiento del atuor: ")
        autor = Autor(nombre=nombre_autor, nacionalidad=nacionalidad,fecha_nacimiento=fecha_nacimiento)
        autor.guardar()
    elif opcion == "2":
        nombre_genero = input ("Ingrese el nombre del geénero: ")
        genero = Genero(nombre=nombre_genero)
        genero.guardar()
    elif opcion == "3":
        titulo = input ("Ingrese el título del libro: ")
        id_autor = input ("Ingrese el id del autor: ")
        id_genero = input ("Ingrese el id del género: ")
        anio_publicacion = input ("Ingrese el año de publicación: ")
        isbn = input ("Ingrese el ISBN: ")
        libro = Libro(titulo=titulo, autor=Autor(id_autor), genero = Genero(id_genero), anio_publicacion=anio_publicacion,isbn=isbn)
        libro.guardar()
    elif opcion == "4":
        nombre = input ("Ingrese el nombre del autor: ")
        Biblioteca.buscar_libros_por_autor(nombre)
    elif opcion == "5" :
        nombre = input ("Ingrese el genero que quieres: ")   
        Biblioteca.buscar_libros_por_genero(nombre)
    elif opcion == "6":
        nombre = input ("Ingrese el titulo del libro: ")
        libro = Libro(titulo=nombre)
        libro.marcar_no_disponible()
    elif opcion == "7":
        nombre = input ("Ingrese el titulo del libro: ")
        libro = Libro(titulo=nombre)
        libro.marcar_disponible()   
    # ME HE QUEDADO EN ESTE PASO, MIRARLO MAÑANA     
    elif opcion == "8":
        eleccion = input ("""Que quieres modificar: 
                  si quieress autor pon 1, si quieres genero pon 2  y si quieres libro por 3: """)  
        if eleccion == "1":
            nombre_autor = input ("Introduce el nombre del autor: ")
            id_buscado = Biblioteca.buscar_id(nombre_autor, "Autores")
            autor = Autor(id_autor=id_buscado, nombre= nombre_autor)
            autor.modificar_autor()
            

    elif opcion =="10":
        print ("Hasta luego")
        exit()
    else: 
        print ("opción no valida")


if __name__ == "__main__":
    main()