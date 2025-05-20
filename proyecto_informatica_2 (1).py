import sqlite3

def crear_tabla():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escuela (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER,
            fecha_nacimiento TEXT
        );
    """)
    conn.commit()
    conn.close()

def agregar_estudiante():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
    conn = sqlite3.connect("escuela.db")
    conn.execute("INSERT INTO escuela (nombre, apellido, edad, fecha_nacimiento) VALUES (?, ?, ?, ?)", 
                 (nombre, apellido, edad, fecha_nacimiento))
    conn.commit()
    conn.close()
    print("Estudiante agregado.")

def modificar_estudiante():
    id = int(input("ID del estudiante a modificar: "))
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_apellido = input("Nuevo apellido: ")
    nueva_edad = int(input("Nueva edad: "))
    nueva_fecha = input("Nueva fecha de nacimiento (dd/mm/aaaa): ")
    conn = sqlite3.connect("escuela.db")
    conn.execute("UPDATE escuela SET nombre=?, apellido=?, edad=?, fecha_nacimiento=? WHERE id=?", 
                 (nuevo_nombre, nuevo_apellido, nueva_edad, nueva_fecha, id))
    conn.commit()
    conn.close()
    print("Estudiante modificado.")

def mostrar_estudiantes():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.execute("SELECT * FROM escuela")
    for fila in cursor:
        print(fila)
    conn.close()

def eliminar_estudiante():
    id = int(input("ID del estudiante a eliminar: "))
    conn = sqlite3.connect("escuela.db")
    conn.execute("DELETE FROM escuela WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print("Estudiante eliminado.")

def buscar_por_apellido():
    apellido = input("Buscar estudiante por apellido: ")
    conn = sqlite3.connect("escuela.db")
    cursor = conn.execute("SELECT * FROM escuela WHERE apellido LIKE ?", ('%' + apellido + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for estudiante in resultados:
            print(estudiante)
    else:
        print("No se encontraron estudiantes con ese apellido.")
    conn.close()

def menu():
    crear_tabla()
    while True:
        print("\n--- MENÚ ESCUELA ---")
        print("1. Agregar estudiante")
        print("2. Modificar estudiante")
        print("3. Mostrar estudiantes")
        print("4. Eliminar estudiante")
        print("5. Buscar por apellido")
        print("6. Salir")

        try:
            opcion = int(input("Elegí una opción: "))
        except ValueError:
            print("Ingresá un número válido.")
            continue

        match opcion:
            case 1:
                agregar_estudiante()
            case 2:
                modificar_estudiante()
            case 3:
                mostrar_estudiantes()
            case 4:
                eliminar_estudiante()
            case 5:
                buscar_por_apellido()
            case 6:
                print("¡Hasta la próxima!")
                break
            case _:
                print("Opción no válida.")

menu()