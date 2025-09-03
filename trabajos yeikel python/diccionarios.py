mascotas = {"nombre" : "tomas", 
            "edad" : 7,
            "raza": "french podlee"}
print(mascotas)


alumnos = {
        1: {"nombre" : "andy", "Apellido" : "borbon", "Edad" : 17 },
        2: {"nombre" : "Pedro", "Apellido" : "pascal", "Edad" : 17},
        3: {"nombre" : "elena", "Apellido" : "morales", "Edad" : 16}
}
print(alumnos)
print(alumnos[2])
print(alumnos[2]["nombre"])

for id_alumno, info in alumnos.items():
    if info["Nombre"]== "Carlos":
        print("si se encuentra en el diccionario")
    else:
        print("no se encuentra en el diccionario")

alumnos.get(3)


alumnos.get(3, {}).get("Nombre")

alumnos(4) = {"nombre" : "Juan", "Apellido" : "Lopez", "Edad" : 15} 

alumnos[2]["edad"] = 14

del alumnos[4]

alumno_eliminado = alumnos.pop(1)

ultimo_alumno = alumnos.popitem()

alumnos.clear()




