from typing import Any, Optional

class List(list):

    __CRITERION_FUNCTION = {}
    
    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def show(self) -> None:
        for element in self:
            print(element)
    
    def search(self, search_value: Any, criterion: str = None) -> Optional[int]:
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:

            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]

            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle -1
            
            middle = (start + end) // 2
    
    # insertar vamos a mantener el append o el insert puede definir un insert_value si lo desean

    def delete_value(self, value, criterion=None) -> Optional[Any]:
        index = self.search(value, criterion)

        return self.pop(index) if index is not None else None

    def sort_by_criterion(self, key_criterion=None) -> None:

        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)

        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar la lista no se como se debe ordenar')

    def size(self) -> int:
        return len(self)

    def filter_contain_on_bio(self, values):
         for element in self:
            bio_min = element.bio.lower()

            bio_limpia = bio_min.replace(".", " ").replace(",", " ")

            palabras_bio = bio_limpia.split()

            if any(value in palabras_bio for value in values):
                print(element)

    def filter_start_with(self, values):
        for element in self:
            if element.name.startswith(values):
                print(element)

    def count_by_field(self, field_name, value):
        contador = 0
        for element in self:
            if element.__dict__.get(field_name) == value:
                contador += 1
        return contador
    
    def unir_L(self,value2):
        for elemento in value2:
            self.append(elemento)
    
    def unir_sin_r(self, value2):
        for elemento in value2:
        # La magia de 'not in' funciona para números, strings y objetos
            if elemento not in self:
                self.append(elemento)
    
    def contar_interseccion(self, otra_lista):
        contador = 0
        vistos = [] # Para evitar contar el mismo repetido varias veces
    
        # Primer ciclo: recorre la lista actual
        for elemento_a in self:
            # Segundo ciclo: recorre la otra lista
            for elemento_b in otra_lista:
                # Compara si son iguales
                if elemento_a == elemento_b:
                    # Verificamos que no lo hayamos contado antes
                    if elemento_a not in vistos:
                        contador += 1
                        vistos.append(elemento_a)
        return contador
    
    def vaciar_mostrando(self):
        # Mientras queden elementos en la lista
        while self.size() > 0:
            # Obtenemos el primer elemento de la lista (el nodo en la cabeza)
            elemento = self[0]
            
            # Eliminamos el primer nodo (el más eficiente)
            self.remove(elemento)
            
            # Imprimimos lo que acabamos de borrar
            print(f"Eliminado: {elemento}")
    
    def invertida(self):
        nueva_lista = List()
        for i in range(len(self) - 1, -1, -1):
            nueva_lista.append(self[i])
        return nueva_lista
    
    def filter_start_with_ape(self, values):
        for element in self:
            if element.lastname.startswith(values):
                print(element)
   
   
    
# class Persona:

#     def __init__(self, nom, ape, ed
# ad):
#         self.nom = nom
#         self.ape = ape
#         self.edad = edad

#     def __str__(self):
#         return f"{self.ape} {self.nom} {self.edad}"


# def by_name(item):
#     return item.nom

# def by_last_name(item):
#     return item.ape

# def by_age(item):
#     return item.edad


# l = List()
# l.add_criterion('name', by_name)
# l.add_criterion('last_name', by_last_name)
# l.add_criterion('age', by_age)


# l.append(Persona("Juan", "Perez", 24))
# l.append(Persona("Dario", "Aron", 12))
# l.append(Persona("Ana", "Blanc", 20))

# print(f'dato eliminado: {l.delete_value("Blanc", "last_name")}')
# l.show()
