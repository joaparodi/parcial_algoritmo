
from tree import BinaryTree
from pokemons_data import pokemons_dict
from list_ import List


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

lista_pokemons = List()

lista_pokemons = List()
for d in pokemons_dict.values():
    lista_pokemons.append(
        Pokemon(d['numero'], d['nombre'], d['tipo'], d['debilidad'], d['mega'], d['gigamax'])
    )

for p in lista_pokemons:
    arbol_nombre.insert_node(p.name, other_value=p)
    arbol_numero.insert_node(p.numero, other_value=p)

for p in lista_pokemons:
    for tipo in p.tipo:
        pos = arbol_tipo.search(tipo)
        if pos is None:
            nueva = List()
            nueva.append(p)
            arbol_tipo.insert_node(tipo, other_value=nueva)
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

num = int(input("ingresa el numero por el cual debo buscar:"))
nodo = arbol_numero.search(num)
if nodo is None:
    print("No existe ese número")
else:
    print(nodo.other_values)


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

arbol_numero.listar()

print("\n--- listado ascendente por nombre------")
arbol_nombre.listar()

print("\n--- Listado por Nivel por Nombre (Breadth-first / by_level) ---")
arbol_nombre.by_level()


# # 5

print("\n--- lista de los pokemones debiles frente a Jolteon------")
arbol_nombre.mostrar_debilidades("Jolteon")
print("\n--- lista de los pokemones debiles frente a Lycanroc------")
arbol_nombre.mostrar_debilidades("Lycanroc")
print("\n--- lista de los pokemones debiles frente a Tyrantrum------")
arbol_nombre.mostrar_debilidades("Tyrantrum")

# # 6

print("\n--- listado de tipo de pokemos y cuantos hay ------")
arbol_nombre.contar_tipos()
print("\n--- cantidad de pokemons con megaevolución: ------")
print(f"{arbol_nombre.contar_mega()}")
print("\n--- cantidad de pokemons con forma gigamax:------")
print(f"{arbol_nombre.contar_gigamax()}")



# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph

g = Graph(is_dir=False)


# 1.
g.add_vertex("Luke Skywalker")
g.add_vertex("Darth Vader")
g.add_vertex("Yoda")
g.add_vertex("Boba Fett")
g.add_vertex("C3PO")
g.add_vertex("Leia")
g.add_vertex("Rey")
g.add_vertex("Kylo Ren")
g.add_vertex("Chewbacca")
g.add_vertex("Han Solo")
g.add_vertex("R2D2")
g.add_vertex("BB8")

# 2. peso basado en episodios juntos
g.add_edge(3, "Luke Skywalker", "Darth Vader")
g.add_edge(5, "Luke Skywalker", "C3PO")
g.add_edge(5, "Luke Skywalker", "Leia")
g.add_edge(5, "Luke Skywalker", "R2D2")
g.add_edge(3, "Luke Skywalker", "Han Solo")
g.add_edge(3, "Luke Skywalker", "Chewbacca")
g.add_edge(2, "Luke Skywalker", "Yoda")

g.add_edge(3, "Darth Vader", "C3PO")
g.add_edge(3, "Darth Vader", "Leia")
g.add_edge(3, "Darth Vader", "R2D2")
g.add_edge(2, "Darth Vader", "Yoda")
g.add_edge(2, "Darth Vader", "Boba Fett")

g.add_edge(3, "Yoda", "C3PO")
g.add_edge(3, "Yoda", "R2D2")
g.add_edge(2, "Yoda", "Leia")

g.add_edge(2, "Boba Fett", "Han Solo")
g.add_edge(2, "Boba Fett", "Chewbacca")
g.add_edge(2, "Boba Fett", "C3PO")
g.add_edge(2, "Boba Fett", "R2D2")

g.add_edge(6, "C3PO", "Leia")
g.add_edge(9, "C3PO", "R2D2")
g.add_edge(4, "C3PO", "Han Solo")
g.add_edge(5, "C3PO", "Chewbacca")
g.add_edge(3, "C3PO", "Rey")
g.add_edge(3, "C3PO", "Kylo Ren")
g.add_edge(3, "C3PO", "BB8")

g.add_edge(6, "Leia", "R2D2")
g.add_edge(4, "Leia", "Han Solo")
g.add_edge(4, "Leia", "Chewbacca")
g.add_edge(2, "Leia", "Rey")
g.add_edge(2, "Leia", "Kylo Ren")

g.add_edge(3, "Rey", "Kylo Ren")
g.add_edge(3, "Rey", "Chewbacca")
g.add_edge(3, "Rey", "BB8")
g.add_edge(3, "Rey", "R2D2")

g.add_edge(3, "Kylo Ren", "Chewbacca")
g.add_edge(3, "Kylo Ren", "BB8")

g.add_edge(4, "Chewbacca", "Han Solo")
g.add_edge(5, "Chewbacca", "R2D2")
g.add_edge(3, "Chewbacca", "BB8")

g.add_edge(4, "Han Solo", "R2D2")

g.add_edge(3, "R2D2", "BB8")


# g.show()
print()

# 3
print("Arbol de expansion minima de Leia")
g.espansion_min("Leia")

print()
print("Arbol de expansion minima de C3PO ")
g.espansion_min("C3PO")

print()
print("Arbol de expansion minima de Yoda")
g.espansion_min("Yoda")



# 4

print()
maximo, pares = g.max_episodios_compartidos()

print(f"Máximo de episodios compartidos: {maximo}")
for a, b in pares:
    print(f"- {a} y {b}")


# 5
print()
print("camino mas corto desde C3PO a R2D2")

g.devolver_camino("C3PO","R2D2")
print()

print("camino mas corto desde Yoda a Darth Vader")
g.devolver_camino("Yoda","Darth Vader")


# 6

print()
print("Personajes que aparecieron en los 9 episodios:")
for personaje in g.personajes_en_todos_los_episodios(9):
    print(f"- {personaje}")




