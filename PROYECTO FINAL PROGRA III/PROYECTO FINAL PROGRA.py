import tkinter as tk
from tkinter import messagebox
import graphviz

class Nodo:
    def __init__(self, estado):
        self.estado = estado
        self.peso = 0
        self.movimientos = {}  # Diccionario para movimientos posibles {movimiento: Nodo}

class Grafo:
    def __init__(self):
        self.nodos = {}

    def obtener_nodo(self, estado):
        if estado not in self.nodos:
            self.nodos[estado] = Nodo(estado)
        return self.nodos[estado]

    def agregar_movimiento(self, estado_actual, movimiento, nuevo_estado):
        nodo_actual = self.obtener_nodo(estado_actual)
        nodo_nuevo = self.obtener_nodo(nuevo_estado)
        nodo_actual.movimientos[movimiento] = nodo_nuevo

class Juego:
    def __init__(self):
        self.grafo = Grafo()
        self.estado_actual = '.........'  # Tablero vacío
        self.movimientos = []  # Para rastrear los movimientos de una partida
        self.turno = 'X'
        self.tablero = ['.'] * 9
        self.partidas_jugadas = 0
        self.historial = []  # Historial de partidas

    def aplicar_movimiento(self, movimiento):
        estado_lista = list(self.estado_actual)
        estado_lista[movimiento] = self.turno
        nuevo_estado = ''.join(estado_lista)
        self.grafo.agregar_movimiento(self.estado_actual, movimiento, nuevo_estado)
        self.estado_actual = nuevo_estado
        self.movimientos.append((self.estado_actual, movimiento, nuevo_estado))
        self.tablero[movimiento] = self.turno
        self.turno = 'O' if self.turno == 'X' else 'X'

    def seleccionar_mejor_movimiento(self):
        nodo_actual = self.grafo.obtener_nodo(self.estado_actual)
        mejor_peso = -float('inf')
        mejor_movimiento = None
        for movimiento in range(9):
            if self.estado_actual[movimiento] == '.':
                nuevo_estado = self.aplicar_movimiento_temp(self.estado_actual, movimiento, 'O')
                nodo_nuevo = self.grafo.obtener_nodo(nuevo_estado)
                if nodo_nuevo.peso > mejor_peso:
                    mejor_peso = nodo_nuevo.peso
                    mejor_movimiento = movimiento
        return mejor_movimiento

    def aplicar_movimiento_temp(self, estado, movimiento, jugador):
        estado_lista = list(estado)
        estado_lista[movimiento] = jugador
        return ''.join(estado_lista)

    def verificar_ganador(self):
        for i in range(3):
            # Verificar filas
            if self.estado_actual[i*3] == self.estado_actual[i*3+1] == self.estado_actual[i*3+2] != '.':
                return self.estado_actual[i*3]
            # Verificar columnas
            if self.estado_actual[i] == self.estado_actual[i+3] == self.estado_actual[i+6] != '.':
                return self.estado_actual[i]
        # Verificar diagonales
        if self.estado_actual[0] == self.estado_actual[4] == self.estado_actual[8] != '.':
            return self.estado_actual[0]
        if self.estado_actual[2] == self.estado_actual[4] == self.estado_actual[6] != '.':
            return self.estado_actual[2]
        if '.' not in self.estado_actual:
            return 'Empate'
        return None

    def actualizar_pesos(self, ganador):
        for estado_actual, movimiento, nuevo_estado in self.movimientos:
            nodo = self.grafo.obtener_nodo(estado_actual)
            if ganador == 'O':
                nodo.peso += 1
            elif ganador == 'X':
                nodo.peso -= 1

    def reiniciar_juego(self):
        self.estado_actual = '.........'
        self.movimientos = []
        self.turno = 'X'
        self.tablero = ['.'] * 9

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.juego = Juego()
        self.buttons = []
        self.puntuacion_jugador = 0
        self.puntuacion_maquina = 0
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font='normal 20 bold', width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Jugar", command=self.reiniciar_juego)
        self.menu.add_command(label="Visualizar Grafo", command=self.visualizar_grafo)
        self.menu.add_command(label="Historial", command=self.ver_historial)
        
        # Crear el submenú de "Integrantes"
        integrantes_menu = tk.Menu(self.menu, tearoff=0)
        integrantes_menu.add_command(label="1. Josué Vinicio Jerez Gómez, 9490-22-1479")
        integrantes_menu.add_command(label="2. Mario Roberto Rompich Yoc, 9490-17-17052")
        self.menu.add_cascade(label="Integrantes", menu=integrantes_menu)
        
        self.menu.add_command(label="Salir", command=self.root.quit)

        self.score_label = tk.Label(self.root, text=f"Jugador: {self.puntuacion_jugador}  Máquina: {self.puntuacion_maquina}", font='normal 15 bold')
        self.score_label.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, index):
        if self.buttons[index]['text'] == '' and self.juego.turno == 'X':
            self.buttons[index]['text'] = 'X'
            self.juego.aplicar_movimiento(index)
            ganador = self.juego.verificar_ganador()
            if ganador:
                self.mostrar_ganador(ganador)
            else:
                self.root.after(1000, self.turno_maquina)  # Retraso de 1 segundo

    def turno_maquina(self):
        movimiento = self.juego.seleccionar_mejor_movimiento()
        if movimiento is not None:
            self.buttons[movimiento]['text'] = 'O'
            self.juego.aplicar_movimiento(movimiento)
            ganador = self.juego.verificar_ganador()
            if ganador:
                self.mostrar_ganador(ganador)

    def mostrar_ganador(self, ganador):
        if ganador == 'Empate':
            messagebox.showinfo("Resultado", "¡Es un empate!")
        else:
            messagebox.showinfo("Resultado", f"¡{ganador} ha ganado!")
            self.actualizar_puntuaciones(ganador)
        self.juego.actualizar_pesos(ganador)
        self.juego.reiniciar_juego()
        self.juego.partidas_jugadas += 1
        self.juego.historial.append(ganador)
        for button in self.buttons:
            button['text'] = ''
        self.actualizar_label_puntuacion()

    def actualizar_puntuaciones(self, ganador):
        if ganador == 'X':
            self.puntuacion_jugador += 100
            self.puntuacion_maquina -= 100
        elif ganador == 'O':
            self.puntuacion_jugador -= 100
            self.puntuacion_maquina += 100

    def actualizar_label_puntuacion(self):
        self.score_label.config(text=f"Jugador: {self.puntuacion_jugador}  Máquina: {self.puntuacion_maquina}")

    def visualizar_grafo(self):
        dot = graphviz.Digraph()
        for estado, nodo in self.juego.grafo.nodos.items():
            dot.node(estado, label=f'{estado}\nPeso: {nodo.peso}')
            for movimiento, nodo_destino in nodo.movimientos.items():
                dot.edge(estado, nodo_destino.estado, label=str(movimiento))
        dot.render('grafo_tictactoe', format='png', view=True)

    def ver_historial(self):
        historial_str = "Historial de Partidas:\n\n"
        for i, resultado in enumerate(self.juego.historial, 1):
            historial_str += f"Partida {i}: {'Ganó el Jugador' if resultado == 'X' else 'Ganó la Máquina' if resultado == 'O' else 'Empate'}\n"
        messagebox.showinfo("Historial de Partidas", historial_str)

    def reiniciar_juego(self):
        self.juego.reiniciar_juego()
        for button in self.buttons:
            button['text'] = ''
        self.actualizar_label_puntuacion()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
