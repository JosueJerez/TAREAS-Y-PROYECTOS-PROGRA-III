import graphviz
import os

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, raiz, valor):
        if raiz is None:
            return Node(valor)
        if valor < raiz.valor:
            raiz.izq = self._insertar_recursivo(raiz.izq, valor)
        else:
            raiz.der = self._insertar_recursivo(raiz.der, valor)
        return raiz

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self._buscar_recursivo(raiz.izq, valor)
        return self._buscar_recursivo(raiz.der, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, raiz, valor):
        if raiz is None:
            return raiz
        if valor < raiz.valor:
            raiz.izq = self._eliminar_recursivo(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self._eliminar_recursivo(raiz.der, valor)
        else:
            if raiz.izq is None:
                return raiz.der
            elif raiz.der is None:
                return raiz.izq
            raiz.valor = self._nodo_valor_minimo(raiz.der).valor
            raiz.der = self._eliminar_recursivo(raiz.der, raiz.valor)
        return raiz

    def _nodo_valor_minimo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                valores = linea.strip().split()  # Dividir la línea en valores separados por espacios
                for valor in valores:
                    try:
                        valor_num = int(valor)
                        self.insertar(valor_num)
                    except ValueError:
                        print(f"Valor no válido encontrado en el archivo: {valor}")

    def convertir_a_binario(self):
        dot = graphviz.Digraph(comment='Árbol de Búsqueda Binario')
        self._convertir_a_binario_recursivo(self.raiz, dot)
        output_dir = os.path.dirname(__file__)
        output_path = os.path.join(output_dir, 'arbol_binario_busqueda.png')
        dot.render(output_path, format='png', cleanup=True)

    def _convertir_a_binario_recursivo(self, raiz, dot):
        if raiz:
            dot.node(str(raiz.valor))
            if raiz.izq:
                dot.edge(str(raiz.valor), str(raiz.izq.valor))
                self._convertir_a_binario_recursivo(raiz.izq, dot)
            if raiz.der:
                dot.edge(str(raiz.valor), str(raiz.der.valor))
                self._convertir_a_binario_recursivo(raiz.der, dot)

def mostrar_menu():
    print("1. Insertar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Cargar desde Archivo")
    print("5. Convertir a Binario")
    print("6. Salir")
    return input("Seleccione una opción: ")

def principal():
    arbol = ArbolBinarioBusqueda()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            valor = int(input("Ingrese el número a insertar: "))
            arbol.insertar(valor)
        elif opcion == '2':
            valor = int(input("Ingrese el número a buscar: "))
            if arbol.buscar(valor):
                print("El número está presente en el árbol.")
            else:
                print("El número no está presente en el árbol.")
        elif opcion == '3':
            valor = int(input("Ingrese el número a eliminar: "))
            arbol.eliminar(valor)
        elif opcion == '4':
            nombre_archivo = input("Ingrese la ruta del archivo: ")
            arbol.cargar_desde_archivo(nombre_archivo)
        elif opcion == '5':
            arbol.convertir_a_binario()
            print("Árbol convertido a binario. Se ha generado el archivo 'arbol_binario_busqueda.png' en la carpeta actual.")
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    principal()
