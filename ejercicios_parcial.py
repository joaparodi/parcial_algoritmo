


from list_ import List
from queue import Queue
from stack import Stack
from random import randint
from super_heroes_data import superheroes


# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.


lista = List()

def cargar(lista : List):
    for hero in superheroes:
        lista.append(hero)

cargar(lista)

# lista.show()

#funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def bus_cap(lista, indice):
    if indice < 0:
        return False
    if lista[indice]["name"] == "Captain America":
        return True
    return bus_cap(lista, indice - 1)

resultado = bus_cap(lista, len(lista) - 1)

print("se encuentra el Capitan America en la lista:")
   
if resultado:
    print("se encontro el Capitan America en la lista")
else:
    print("no se encontro el Capitan America")



#funcion recursiva para listar los superheroes de la lista.

def listar_superheroes(lista, indice):
    if indice < 0:
        return
    print(lista[indice]["name"])
    listar_superheroes(lista, indice - 1)


listar_superheroes(lista, len(lista) - 1)








# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# Listar los superheores que comienzan con  Bl, G, My, y W.
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# Listado de superheroes ordenados por fecha de aparación.
# Modificar el nombre real de Ant Man a Scott Lang.
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

class Personajes:
    def __init__(self,nombre,alias,nombre_real,bio,aparicion,villano):
        self.name = nombre
        self.alias = alias
        self.real_name = nombre_real
        self.bio = bio
        self.first_appearance = aparicion
        self.is_villain = villano
    
    def __str__(self):
        return f"nombre:{self.name}|alias:{self.alias}|nombre real:{self.real_name}|biografia breve:{self.bio}|primera aparicion:{self.first_appearance}|villano:{self.is_villain}"   
    
        
lista_P = List()

def cargar_lista(lista_P: List):
    for hero in superheroes:
        lista_P.append(Personajes(hero["name"],hero["alias"],hero["real_name"],hero["short_bio"],hero["first_appearance"],hero["is_villain"]))        

cargar_lista(lista_P)
        
        
# Listado ordenado de manera ascendente por nombre de los personajes.

def by_name(item):
    return item.name       
        
lista_P.add_criterion("name",by_name) 

lista_P.sort_by_criterion("name")      
        
lista_P.show()       
        
        
# Determinar en que posicion esta The Thing y Rocket Raccoon.
the_thing = lista_P.search("The Thing", 'name')

if the_thing is not None:
    print(f'{lista_P[the_thing].name} esta en la posicion {the_thing}')
else:
    print('no esta en la lista')
        
rocket_raccoon = lista_P.search("Rocket Raccoon", "name")

if rocket_raccoon is not None:
    print(f'{lista_P[rocket_raccoon].name} esta en la posicion {rocket_raccoon}')
else:
    print('no esta en la lista')
    
print()
        
# Listar todos los villanos de la lista.


def lis_villanos(lista_P : List):
    aux = List()
    for pj in lista_P:
        if pj.is_villain == True:
            aux.append(pj)
    return aux

villanos = lis_villanos(lista_P)

print("lista de villanos:")

if villanos.size() > 0 :
    villanos.show()
else:
    print("no hay ningun villano en la lista")
    
print()


# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

def aparicion(lista_P : List):
    aux = Queue()
    for pj in lista_P:
        if pj.is_villain and pj.first_appearance < 1980:
            aux.arrive(pj)
    return aux
        
p_aperecieron = aparicion(lista_P)
print("lista de villanos que aparecieron antes de 1980:")
print()

if p_aperecieron.size() > 0 :
    p_aperecieron.show()
else:
    print("ningun villano aparecion antes de 1980")

print()


# Listar los superheores que comienzan con  Bl, G, My, y W.

lista_P.filter_start_with(("Bl","G","My","W"))
print()

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes

def by_real_name(item):
    if item.real_name is None:
        return "" 
    return item.real_name

print("listado segun el orden de los nombres reales: ")
print()

lista_P.add_criterion("real_name",by_real_name)

lista_P.sort_by_criterion("real_name")
lista_P.show()
print()

# Listado de superheroes ordenados por fecha de aparación.

def by_appearance(item):
    return item.first_appearance 

print("lista de superheros ordenados por fecha de aparicion")

lista_P.add_criterion("first_appearance", by_appearance)
lista_P.sort_by_criterion("first_appearance")
lista_P.show()
print()

# Modificar el nombre real de Ant Man a Scott Lang.

ant_man = lista_P.search("Ant Man", 'name')
if ant_man is not None:
    lista_P[ant_man].real_name = 'Scott Lang'

print("lista pero con el nombre de ant man modificado")
print()
# lista_P.show()
print()

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

print("personajes que en su biografia contiene time-traveling o suit")
print()
lista_P.filter_contain_on_bio(['time-traveling','suit'])



# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

print()

# Como delete_value retorna el objeto eliminado (porque self.pop retorna el elemento)
electro_eliminado = lista_P.delete_value("Electro", "name")

if electro_eliminado is not None:
    print(f"Personaje eliminado: {electro_eliminado.name}")
    print(f"Información: {electro_eliminado}") 
else:
    print("Electro no estaba en la lista.")

print()

zemo_eliminado = lista_P.delete_value("Baron Zemo", "name")

if zemo_eliminado is not None:
    print(f"Personaje eliminado: {zemo_eliminado.name}")
    print(f"Información: {zemo_eliminado}")
else:
    print("Baron Zemo no estaba en la lista.")



