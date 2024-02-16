import graphviz

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.ultimo_nodo is None:
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo.siguiente = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo

    def eliminar_por_valor(self, valor):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            if nodo_actual.nombre == valor or nodo_actual.apellido == valor or nodo_actual.carnet == valor:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.primer_nodo = nodo_actual.siguiente
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.ultimo_nodo = nodo_actual.anterior
                return
            nodo_actual = nodo_actual.siguiente
        print("El valor no se encontró en la lista.")

    def mostrar_lista(self):
        nodo_actual = self.primer_nodo
        print("None", end=" <- ")
        while nodo_actual:
            print(f"{nodo_actual.nombre} {nodo_actual.apellido} {nodo_actual.carnet}", end=" <-> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def generar_grafo(self):
        grafo = graphviz.Digraph(format='png')
        nodo_actual = self.primer_nodo
        while nodo_actual:
            grafo.node(str(nodo_actual.nombre), label=f"{nodo_actual.nombre} {nodo_actual.apellido} {nodo_actual.carnet}")
            if nodo_actual.siguiente:
                grafo.edge(str(nodo_actual.nombre), str(nodo_actual.siguiente.nombre))
            if nodo_actual.anterior:
                grafo.edge(str(nodo_actual.nombre), str(nodo_actual.anterior.nombre))
            nodo_actual = nodo_actual.siguiente
        return grafo

# Función para interactuar con la lista mediante CLI
def menu_interactivo(lista):
    while True:
        print("\nMenú:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Mostrar lista")
        print("5. Generar gráfico")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == "3":
            valor = input("Ingrese el valor a eliminar: ")
            lista.eliminar_por_valor(valor)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            grafo = lista.generar_grafo()
            grafo.render(filename='lista_doblemente_enlazada', directory='./', cleanup=True, format='png')
            print("Se generó el gráfico de la lista doblemente enlazada.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    menu_interactivo(lista)
