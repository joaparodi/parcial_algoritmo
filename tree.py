from typing import Any, Optional

from queue import Queue
from heap import HeapMin


class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0 #altura del nodo, se inicializa en 0 para un nodo hoja
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value, root.height)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root is None:
                
            
                if root.left is not None:
                    __postorden(root.left)
            
                if root.right is not None:
                    __postorden(root.right)
                print(root.value)
            

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()

    
    def proxy_search(self, prefix: str) -> None:
        
        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix in str(root.value).lower():
                print(f"pokemon : {root.value}-- Datos: {root.other_values}")
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

           
    def buscar_por_tipo(self, tipo):
        nodo = self.search(tipo)
        if nodo is None:
            print("No hay Pokémon de ese tipo")
        else:
            for p in nodo.other_values:
                print(f"- {p.name} (Nº {p.numero})")

    def mostrar_debilidades(self, nombre):
        nodo = self.search(nombre)
        if nodo is None:
            print("Pokémon no encontrado")
            return
        tipos = nodo.other_values.tipo

        def __recorrer(root):
            if root.left is not None:
                __recorrer(root.left)

            p = root.other_values
            if any(t in p.debilidad for t in tipos):
                print(f"- {p.name} (Nº {p.numero})")

            if root.right is not None:
                __recorrer(root.right)

        print(f"\nDébiles frente a {nombre} ({', '.join(tipos)}):")
        if self.root is not None:
            __recorrer(self.root)
                
    
    def contar_tipos(self):
        conteo = {}

        def __contar_tipos(root):
            if root.left is not None:
                __contar_tipos(root.left)

            for tipo in root.other_values.tipo:        
                if tipo in conteo:
                    conteo[tipo] += 1                  
                else:
                    conteo[tipo] = 1                  

            if root.right is not None:
                __contar_tipos(root.right)

        if self.root is not None:
            __contar_tipos(self.root)

        heap = HeapMin()
        for tipo, cantidad in conteo.items():
            heap.arrive(tipo, cantidad)

        print("Cantidad de Pokémon por tipo:")
        while heap.size() > 0:
            prioridad, tipo = heap.attention()
            print(f"- {tipo}: {prioridad}")
                
                
    def contar_mega(self):
        def __contar_mega(root):
            cant = 0
            if root.left is not None:
                cant += __contar_mega(root.left)

            if root.other_values.mega:
                cant += 1

            if root.right is not None:
                cant += __contar_mega(root.right)
            return cant

        if self.root is None:
            return 0
        return __contar_mega(self.root)


    def contar_gigamax(self):
        def __contar_gigamax(root):
            cant = 0
            if root.left is not None:
                cant += __contar_gigamax(root.left)

            if root.other_values.gigamax:
                cant += 1

            if root.right is not None:
                cant += __contar_gigamax(root.right)
            return cant

        if self.root is None:
            return 0
        return __contar_gigamax(self.root)           
                
                
                
                
                
                
                
                
                
            
                
        
