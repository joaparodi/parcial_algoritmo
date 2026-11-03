
from tree import BinaryTree
from pokemons_data import pokemons_dict



# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# los índices de cada uno de los árboles deben ser nombre, número y tipo;
# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# determinar cuantos Pokémons tienen megaevolucion.
# determinar cuantos Pokémons tiene forma gigamax.
# cargue al menos 100 Pokémons.

class Pokemon:
    def __init__(self, numero, nombre, tipo, debilidad, mega, gigamax):
        self.numero = numero
        self.name = nombre
        self.tipo = tipo
        self.debilidad = debilidad
        self.mega = mega
        self.gigamax = gigamax

    def __str__(self):
        return f"Nº {self.numero} - {self.name} (Tipos: {self.tipo})"


# 1

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

lista_pokemons = [
    Pokemon(d['numero'], d['nombre'], d['tipo'], d['debilidad'], d['mega'], d['gigamax'])
    for d in pokemons_dict.values()
]

for p in lista_pokemons:
    arbol_nombre.insert_node(p.name, other_value=p)
    arbol_numero.insert_node(p.numero, other_value=p)

for p in lista_pokemons:
    for tipo in p.tipo:
        pos = arbol_tipo.search(tipo)
        if pos is None:
            arbol_tipo.insert_node(tipo, other_value=[p])
        else:
            pos.other_values.append(p)


print("¡Árboles cargados exitosamente con", len(pokemons_dict), "Pokémon!")

# print()
# arbol_nombre.inorden()
# print()
# # arbol_numero.inorden()
# print()
# arbol_tipo.postorden()

# 2 

print()
nom = input("ingresa el nombre por el cual quiere buscar :")
arbol_nombre.proxy_search(nom.lower())
print()
num = input("ingresa el numero por el cual debo buscar:")
arbol_numero.proxy_search(num)


# 3


print("\n--- Pokémons de tipo Fuego ---")
arbol_tipo.buscar_por_tipo("Fuego")

print("\n--- Pokémons de tipo fantasma ---")
arbol_tipo.buscar_por_tipo("Fantasma")

print("\n--- Pokémons de tipo Acero---")
arbol_tipo.buscar_por_tipo("Acero")

print("\n--- Pokémons de tipo Electrico ---")
arbol_tipo.buscar_por_tipo("Eléctrico")

# 4

print("\n--- Listado ascendente por Número (Inorden en árbol_numero) ---")

arbol_numero.inorden()

print("\n--- listado ascendente por nombre------")
arbol_nombre.inorden()

print("\n--- Listado por Nivel por Nombre (Breadth-first / by_level) ---")
arbol_nombre.by_level()


# # 5

arbol_nombre.mostrar_debilidades("Jolteon")
arbol_nombre.mostrar_debilidades("Lycanroc")
arbol_nombre.mostrar_debilidades("Tyrantrum")

# # 6


for tipo in ["Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo", "Lucha", "Veneno", "Tierra",
     "Volador", "Psíquico", "Bicho", "Roca", "Fantasma", "Dragón", "Siniestro", "Acero", "Hada"]:
    print(f"- {tipo}: {arbol_nombre.contar_tipo(tipo)}")

