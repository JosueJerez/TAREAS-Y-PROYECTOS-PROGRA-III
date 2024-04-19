from flask import Flask, request, jsonify
import csv
import datetime

app = Flask(__name__)

class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if not node:
            return
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _rotate_right(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if not node:
            return TreeNode(key, data)

        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            return node

        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Objeto global para el árbol AVL
avl_tree = AVLTree()

# Ruta para cargar registros desde un archivo CSV
@app.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    data = request.json
    csv_file = data.get('archivo_csv')
    if not csv_file:
        return jsonify({'error': 'No se proporcionó un archivo CSV'}), 400

    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir la cadena de fecha y hora en un objeto datetime
            date_rptd_str = row['Date Rptd']
            try:
                date_rptd = datetime.datetime.strptime(date_rptd_str, '%m/%d/%Y %I:%M:%S %p')
            except ValueError:
                return jsonify({'error': f'Formato de fecha y hora inválido: {date_rptd_str}'}), 400

            data = row['data']
            avl_tree.insert(date_rptd, data)

    return jsonify({'message': 'Registros cargados correctamente'}), 200

# Ruta para insertar un registro manualmente
@app.route('/insertar_registro', methods=['POST'])
def insertar_registro():
    data = request.json
    date_rptd = int(data.get('Date Rptd'))
    data = data.get('data')
    if date_rptd is None or data is None:
        return jsonify({'error': 'Se requiere una fecha reportada (Date Rptd) y datos (data) para insertar un registro'}), 400

    avl_tree.insert(date_rptd, data)
    return jsonify({'message': 'Registro insertado correctamente'}), 201

# Ruta para buscar un registro por su identificador
@app.route('/buscar_registro/<int:identificador>', methods=['GET'])
def buscar_registro(identificador):
    data = avl_tree.search(identificador)
    if data is not None:
        return jsonify({'data': data}), 200
    else:
        return jsonify({'error': 'Registro no encontrado'}), 404

# Ruta para mostrar información del grupo
@app.route('/info_grupo', methods=['GET'])
def info_grupo():
    info = {
        'integrantes': [
            {'nombre': 'Nombre 1', 'carnet': 'Carnet 1', 'contribuciones': 'Contribuciones 1'},
            {'nombre': 'Nombre 2', 'carnet': 'Carnet 2', 'contribuciones': 'Contribuciones 2'}
        ]
    }
    return jsonify(info), 200

# Ruta para la página de inicio
@app.route('/', methods=['GET'])
def pagina_inicio():
    return '¡Bienvenido a mi API! Puedes acceder a las siguientes rutas: /cargar_csv, /insertar_registro, /buscar_registro/<identificador>, /info_grupo'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
