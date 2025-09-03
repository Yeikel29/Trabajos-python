mi_diccionario = {"nombre" : "Yeikel", "Edad" : 16, "curso" : "python"}

print(mi_diccionario)

print(mi_diccionario["nombre"])

print(mi_diccionario["Edad"])


mi_diccionario["Edad"]+= 1

mi_diccionario["ciudad"] = "puriscal"

productos = {"manzana": 1.50, "pan": 2.00, "leche": 3.20}

print(list(productos.keys()))




biblioteca = {
    "El señor de los anillos": {
        "autor": "J.R.R. Tolkien",
        "año_publicacion": 1954,
        "disponible": True
    },
    "Cien años de soledad": {
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967,
        "disponible": False
    }
}