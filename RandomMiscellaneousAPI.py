### DOCUMENTACIÓN ###
# Nombre: RandomMiscellaneousAPI.py
# Autor: Fernando Franco Zago
# Fecha: 05/05/2025
# Versión: 0.1.3
# Descripción: RandomMiscellaneousAPI es una API desarrollada con Flask que
#    permite generar diversos datos aleatorios útiles para pruebas, simulaciones,
#    juegos, educación o desarrollo de software. Entre sus funcionalidades se
#    incluyen la generación de números aleatorios, lanzamientos de moneda, selección
#    aleatoria de elementos desde listas, coordenadas geográficas, fechas,
#    contraseñas seguras, colores en formato hexadecimal y mucho más. La API es
#    altamente configurable y está diseñada para ofrecer respuestas claras,
#    estructuradas y listas para integrarse en sistemas frontend, scripts 
#    automatizados o entornos de desarrollo.
# Requisitos: pip install Flask, pip install flasgger
# Librerías: Flask, jsonify, request, Swagger, randint, sample, uniform, choices, datetime, timedelta
#####################

### LIBRERÍAS ###
# Instaladas
from flask import Flask, jsonify, request
from flasgger import Swagger
# Nativas
from random import randint, sample, uniform, choices
from datetime import datetime, timedelta
#################

app = Flask(__name__)

# Configuración de Swagger
swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "RandomMiscellaneousAPI",
        "description": "RandomMiscellaneousAPI es una API desarrollada con Flask que permite generar diversos datos aleatorios útiles para pruebas, simulaciones, juegos, educación o desarrollo de software. Entre sus funcionalidades se incluyen la generación de números aleatorios, lanzamientos de moneda, selección aleatoria de elementos desde listas, coordenadas geográficas, fechas, contraseñas seguras, colores en formato hexadecimal y mucho más. La API es altamente configurable y está diseñada para ofrecer respuestas claras, estructuradas y listas para integrarse en sistemas frontend, scripts automatizados o entornos de desarrollo.",
        "version": "0.1.3",
        "contact": {
            "name": "Fernando Franco Zago"
        }
    },
    "host": "localhost:5000",  # O cámbialo por tu dominio en producción
    "basePath": "/"
}

swagger = Swagger(app, template=swagger_config)

### API DOC ###
# Nombre: home
# Descripción: Devuelve la documentación de la API.
# Respuesta: JSON con la documentación de la API.
@app.route('/')
def home():
    documentacion = {
        "nombre": "RandomMiscellaneousAPI.py",
        "autor": "Fernando Franco Zago",
        "fecha": "05/05/2025",
        "version": "0.1.3",
        "descripcion": "RandomMiscellaneousAPI es una API desarrollada con Flask que permite generar diversos datos aleatorios útiles para pruebas, simulaciones, juegos, educación o desarrollo de software. Entre sus funcionalidades se incluyen la generación de números aleatorios, lanzamientos de moneda, selección aleatoria de elementos desde listas, coordenadas geográficas, fechas, contraseñas seguras, colores en formato hexadecimal y mucho más. La API es altamente configurable y está diseñada para ofrecer respuestas claras, estructuradas y listas para integrarse en sistemas frontend, scripts automatizados o entornos de desarrollo.",
        "requisitos": ["pip install Flask", "pip install flasgger"],
        "librerias": {
            "flask": ["Flask", "jsonify", "request"],
            "flasgger": ["Swagger"],
            "random": ["randint", "sample", "uniform", "choices"],
            "datetime": ["datetime", "timedelta"]
        }
    }
    return jsonify(documentacion)

### API ###
# Nombre: NumAleatorio
# Tipo: GET
# Descripción: Genera números aleatorios entre un límite inferior y superior.
# Parámetros:
#   - lim_inferior: Límite inferior (por defecto 0).
#   - lim_superior: Límite superior (por defecto 100).
#   - cantidad: Cantidad de números aleatorios a generar (por defecto 1).
# Respuesta: JSON con los números aleatorios generados.
###########
@app.route('/api/NumAleatorio', methods=['GET'])
def NumAleatorio():
    """
    Genera números aleatorios entre un límite inferior y superior.
    ---
    parameters:
      - name: lim_inferior
        in: query
        type: integer
        required: false
        default: 1
      - name: lim_superior
        in: query
        type: integer
        required: false
        default: 100
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un número aleatorio generado
        examples:
          application/json: {"aleatorios":[88],"cantidad":1,"error":false,"status":200}
      400:
        description: Límite inferior mayor o igual al límite superior
        examples:
          application/json: {"code":1002,"error":true,
          "message":"El límite inferior debe ser menor que el superior.","status":400}
    """
    lim_inferior = request.args.get('lim_inferior', 1, type=int)
    lim_superior = request.args.get('lim_superior', 100, type=int)
    cantidad = request.args.get('cantidad', 1, type=int)

    if lim_inferior >= lim_superior:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'El límite inferior debe ser menor que el superior.',
            'code': 1002
        }), 400

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a cero.',
            'code': 1001
        }), 400

    numeros = [randint(lim_inferior, lim_superior) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'aleatorios': numeros,
        'cantidad': cantidad
        }), 200

### API ###
# Nombre: NumDecimalAleatorio
# Tipo: GET
# Descripción: Genera números decimales aleatorios entre un límite inferior y superior.
# Parámetros:
#   - lim_inferior: Límite inferior (por defecto 0).
#   - lim_superior: Límite superior (por defecto 100).
#   - decimales: Cantidad de decimales (por defecto 2).
#   - cantidad: Cantidad de números decimales aleatorios a generar (por defecto 1).
# Respuesta: JSON con los números decimales aleatorios generados.
############
@app.route('/api/NumDecimalAleatorio', methods=['GET'])
def NumDecimalAleatorio():
    """
    Genera números decimales aleatorios entre un límite inferior y superior.
    ---
    parameters:
      - name: lim_inferior
        in: query
        type: integer
        required: false
        default: 1
      - name: lim_superior
        in: query
        type: integer
        required: false
        default: 100
      - name: decimales
        in: query
        type: integer
        required: false
        default: 2
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un número decimal aleatorio generado
        examples:
          application/json: {"aleatorios":[26.83],"cantidad":1,"error":false,"status":200}
      400:
        description: Límite inferior mayor o igual al límite superior
        examples:
          application/json: {"code":1003,"error":true,
          "message":"El límite inferior debe ser menor que el superior.","status":400}
    """
    lim_inferior = request.args.get('lim_inferior', 1, type=float)
    lim_superior = request.args.get('lim_superior', 100, type=float)
    decimales = request.args.get('decimales', 2, type=int)
    cantidad = request.args.get('cantidad', 1, type=int)

    if lim_inferior >= lim_superior:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'El límite inferior debe ser menor que el superior.',
            'code': 1003
        }), 400

    if decimales < 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Los decimales deben ser mayores a cero.',
            'code': 1002
        }), 400

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a cero.',
            'code': 1001
        }), 400

    numeros = [round(uniform(lim_inferior, lim_superior), decimales) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'aleatorios': numeros,
        'cantidad': cantidad
        }), 200

### API ###
# Nombre: BarajaAleatoria
# Tipo: GET
# Descripción: Genera manos de cartas aleatorias de una baraja inglesa.
# Parámetros:
#   - cartas_por_mano: Cantidad de cartas por mano (por defecto 1).
#   - manos: Cantidad de manos a repartir (por defecto 1).
# Respuesta: JSON con las manos de cartas generadas.
###########
@app.route('/api/BarajaAleatoria', methods=['GET'])
def BarajaAleatoria():
    """
    Genera manos de cartas aleatorias de una baraja inglesa.
    ---
    parameters:
      - name: cartas_por_mano
        in: query
        type: integer
        required: false
        default: 1
      - name: manos
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Una carta aleatoria generada
        examples:
          application/json: {"cartas_por_mano":1,"error":false,"manos":[{"mano_1":["10♣"]}],
          "status":200,"total_cartas":1}
      400:
        description: No hay suficientes cartas en la baraja para repartir sin repetir.
        examples:
          application/json: {"code":1002,"error":true,
          "message":"No hay suficientes cartas en la baraja para repartir sin repetir.","status":400}
    """
    cartas_por_mano = request.args.get('cartas', 1, type=int)
    manos = request.args.get('manos', 1, type=int)

    if cartas_por_mano <= 0 or manos <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Las cantidades de manos y cartas deben ser mayores a 0.',
            'code': 1001
            }), 400

    baraja = [
        "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
        "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"
    ]

    total_cartas = cartas_por_mano * manos

    if total_cartas > len(baraja):
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'No hay suficientes cartas en la baraja para repartir sin repetir.',
            'code': 1002
            }), 400

    cartas_repartidas = sample(baraja, total_cartas)
    manos_repartidas = []

    for i in range(manos):
        inicio = i * cartas_por_mano
        fin = inicio + cartas_por_mano
        manos_repartidas.append({
            f"mano_{i+1}": cartas_repartidas[inicio:fin]
        })

    return jsonify({
        'status': 200,
        'error': False,
        'manos': manos_repartidas,
        'cartas_por_mano': cartas_por_mano,
        'total_cartas': total_cartas
    }), 200

### API ###
# Nombre: LanzamientosMoneda
# Tipo: GET
# Descripción: Genera lanzamientos de moneda con resultados entre cara o cruz.
# Parámetros:
#   - lanzamientos: Cantidad de lanzamientos de moneda (por defecto 1).
# Respuesta: JSON con los lanzamientos de moneda.
###########
@app.route('/api/LanzamientosMoneda', methods=['GET'])
def LanzamientoMoneda():
    """
    Genera lanzamientos de moneda con resultados entre cara o cruz.
    ---
    parameters:
      - name: lanzamientos
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un lanzamiento de moneda
        examples:
          application/json: {"error":false,"lanzamientos":[{"lanzamiento_1":"Cruz"}],
          "status":200,"total_lanzamientos":1}
      400:
        description: Cantidad de lanzamientos menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de lanzamientos debe ser mayor a 0.","status":400}
    """
    lanzamientos = request.args.get('lanzamientos', 1, type=int)

    if lanzamientos <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de lanzamientos debe ser mayor a 0.',
            'code': 1001
            }), 400

    lanzamientos_dict = {}
    for i in range(1, lanzamientos + 1):
        lanzamientos_dict[f"lanzamiento_{i}"] = "Cara" if uniform(0, 1) >= 0.5 else "Cruz"

    respuesta = {
        "status": 200,
        "error": False,
        "lanzamientos": [lanzamientos_dict],
        "total_lanzamientos": lanzamientos
    }

    return jsonify(respuesta), 200

### API ###
# Nombre: LanzamientosDado
# Tipo: GET
# Descripción: Genera lanzamientos de un dado con resultados entre 1 y 6.
# Parámetros:
#   - lanzamientos: Cantidad de lanzamientos de dado (por defecto 1).
#   - dados: Cantidad de dados a lanzar por lanzamiento (por defecto 1).
# Respuesta: JSON con los lanzamientos de dado.
###########

@app.route('/api/LanzamientosDado', methods=['GET'])
def LanzamientoDado():
    """
    Genera lanzamientos de un dado con resultados entre 1 y 6.
    ---
    parameters:
      - name: lanzamientos
        in: query
        type: integer
        required: false
        default: 1
      - name: dados
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un lanzamiento de un dado
        examples:
          application/json: {"dados_por_lanzamiento":1,"error":false,
          "lanzamientos":[{"lanzamiento_1":[4]}],"status":200,"total_lanzamientos":1}
      400:
        description: Cantidad de dados menor o igual a 0
        examples:
          application/json: {"code":1002,"error":true,
          "message":"La cantidad de dados debe ser mayor a 0.","status":400}
    """
    lanzamientos = request.args.get('lanzamientos', 1, type=int)
    dados = request.args.get('dados', 1, type=int)

    if lanzamientos <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de lanzamientos debe ser mayor a 0.',
            'code': 1001
            }), 400
    
    if dados <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de dados debe ser mayor a 0.',
            'code': 1002
            }), 400

    lanzamientos_dict = {}
    for i in range(1, lanzamientos + 1):
        lanzamientos_dict[f"lanzamiento_{i}"] = [randint(1, 6) for _ in range(dados)]

    respuesta = {
        "status": 200,
        "error": False,
        "lanzamientos": [lanzamientos_dict],
        "total_lanzamientos": lanzamientos,
        "dados_por_lanzamiento": dados
    }

    return jsonify(respuesta), 200

### API ###
# Nombre: DecisionAleatoria
# Tipo: GET
# Descripción: Genera decisiones aleatorias entre Si y No.
# Parámetros:
#   - cantidad: Cantidad de decisiones a generar (por defecto 1).
#Respuesta: JSON con las decisiones generadas.
###########
@app.route('/api/DecisionAleatoria', methods=['GET'])
def DecisionAleatoria():
    """
    Genera decisiones aleatorias entre Si y No.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Una decisión aleatoria
        examples:
          application/json: {"decisiones":[{"decisión_1":"No"}],
          "error":false,"status":200,"total_decisiones":1}
      400:
        description: Cantidad de decisiones menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de decisiones debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de decisiones debe ser mayor a 0.',
            'code': 1001,
            }), 400

    decisiones = ["Si", "No"]
    decisiones_dict = {}

    for i in range(1, cantidad + 1):
        decisiones_dict[f"decisión_{i}"] = sample(decisiones, 1)[0]

    respuesta = {
        "status": 200,
        "error": False,
        "decisiones": [decisiones_dict],
        "total_decisiones": cantidad
    }

    return jsonify(respuesta), 200

### API ###
# Nombre: LetraAleatoria
# Tipo: GET
# Descripción: Genera letras aleatorias del alfabeto inglés entre A y Z.
# Parámetros:
#   - cantidad: Cantidad de letras a generar (por defecto 1).
# Respuesta: JSON con las letras generadas.
###########
@app.route('/api/LetraAleatoria', methods=['GET'])
def LetraAleatoria():
    """
    Genera letras aleatorias del alfabeto inglés entre A y Z.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Una letra aleatoria
        examples:
          application/json: {"cantidad":1,"error":false,"letras":["U"],"status":200}
      400:
        description: Cantidad de letras menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de letras debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de letras debe ser mayor a 0.',
            'code': 1001
            }), 400

    letras = [chr(randint(65, 90)) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'letras': letras,
        'cantidad': cantidad
        }), 200

### API ###
# Nombre: PiedraPapelTijera
# Tipo: GET
# Descripción: Genera una decisión aleatoria entre piedra, papel o tijera.
# Respuesta: JSON con la decisión generada.
###########
@app.route('/api/PiedraPapelTijera', methods=['GET'])
def PiedraPapelTijera():
    """
    Genera una decisión aleatoria entre piedra, papel o tijera.
    ---
    responses:
      200:
        description: Una opción del juego de piedra, papel o tijera
        examples:
          application/json: {"decision":"Piedra","error":false,"status":200}
    """
    opciones = ["Piedra", "Papel", "Tijera"]
    decision = sample(opciones, 1)[0]

    return jsonify({
        'status': 200,
        'error': False,
        'decision': decision
        }), 200

### API ###
# Nombre: CoordenadaAleatoria
# Tipo: GET
# Descripción: Genera coordenadas geográficas aleatorias con latitud y longitud.
# Parámetros:
#   - cantidad: Cantidad de coordenadas a generar (por defecto 1).
# Respuesta: JSON con las coordenadas generadas.
###########
@app.route('/api/CoordenadaAleatoria', methods=['GET'])
def CoordenadasAleatorias():
    """
    Genera coordenadas geográficas aleatorias con latitud y longitud.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Una coordenada geográfica
        examples:
          application/json: {"cantidad":1,
          "coordenadas":{"coordenada_1":{"latitud":-37.192801,"longitud":-149.659038}},
          "error":false,"status":200}
      400:
        description: Cantidad de coordenadas menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de coordenadas debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de coordenadas debe ser mayor a 0.',
            'code': 1001,
            }), 400

    resultado = {}
    for i in range(1, cantidad + 1):
        latitud = round(uniform(-89.999999, 89.999999), 6)
        longitud = round(uniform(-179.999999, 179.999999), 6)
        resultado[f'coordenada_{i}'] = {
            'latitud': latitud,
            'longitud': longitud
        }

    return jsonify({
        'status' : 200,
        'error' : False,
        'coordenadas' : resultado,
        'cantidad' : cantidad
        }), 200

### API ###
# Nombre: BinarioAleatorio
# Tipo: GET
# Descripción: Genera un número binario aleatorio de una longitud específica.
# Parámetros:
#   - longitud: Longitud del número binario (por defecto 1).
#   - cantidad: Cantidad de números binarios a generar (por defecto 1).
# Respuesta: JSON con los números binarios generados.
###########
@app.route('/api/BinarioAleatorio', methods=['GET'])
def BinarioAleatorio():
    """
    Genera un número binario aleatorio de una longitud específica.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
      - name: longitud
        in: query
        type: integer
        required: false
        default: 8
    responses:
      200:
        description: Un numero binario de longitud 8
        examples:
          application/json: {"binarios":["01010110"],"cantidad":1,
          "error":false,"longitud":8,"status":200}
      400:
        description: Longitud menor o igual a 0
        examples:
          application/json: {"code":1002,"error":true,
          "message":"La longitud debe ser mayor a 0.","status":400}
    """
    longitud = request.args.get('longitud', 8, type=int)
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001
            }), 400
    
    if longitud <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La longitud debe ser mayor a 0.',
            'code': 1002
            }), 400

    binarios = [''.join(choices('01', k=longitud)) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'binarios': binarios,
        'longitud': longitud,
        'cantidad': cantidad
    }), 200

### API ###
# Nombre: SeleccionAleatoria
# Tipo: GET
# Descripción: Selecciona aleatoriamente elementos de una lista dada.
# Parámetros:
#   - valores: Lista de elementos a seleccionar.
#   - cantidad: Cantidad de elementos a seleccionar (por defecto 1).
#   - unicos: Si se deben seleccionar elementos únicos (por defecto 1).
# Respuesta: JSON con los elementos seleccionados.
###########
@app.route('/api/SeleccionAleatoria', methods=['GET'])
def SeleccionAleatoria():
    """
    Selecciona aleatoriamente elementos de una lista dada.
    ---
    parameters:
      - name: valores
        in: query separado por comas
        type: string
        required: true
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
      - name: unicos
        in: query [0 - Valores repetibles, 1 - Valores únicos]
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Una selección aleatoria de 3 colores
        examples:
          application/json: {"cantidad":1,"error":false,
          "seleccionados":{"seleccion_1":"rojo"},"status":200,"unicos":true,
          "valores":["rojo","verde","azul"]}
      400:
        description: Lista de valores no proporcionada
        examples:
          application/json: {"code":1002,"error":true,
          "message":"Debes proporcionar una lista de valores separados por comas.","status":400}
    """
    valores_str = request.args.get('valores')
    cantidad = request.args.get('cantidad', 1, type=int)
    unicos = request.args.get('unicos', 1, type=int)

    if not valores_str:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Debes proporcionar una lista de valores separados por comas.',
            'code': 1002
        }), 400

    valores = valores_str.split(',')

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001
        }), 400

    if unicos:
        if cantidad > len(valores):
            return jsonify({
                'status': 400,
                'error': True,
                'message': 'La cantidad solicitada excede el número de valores disponibles sin repetir.',
                'code': 1003
            }), 400
        seleccion = sample(valores, cantidad)
    else:
        seleccion = choices(valores, k=cantidad)

    seleccion_formateada = {
        f"seleccion_{i+1}": valor for i, valor in enumerate(seleccion)
    }

    return jsonify({
        'valores': valores,
        'status': 200,
        'error': False,
        'seleccionados': seleccion_formateada,
        'cantidad': cantidad,
        'unicos': bool(unicos)
    }), 200

### API ###
# Nombre: ContraseñaAleatoria
# Tipo: GET
# Descripción: Genera una contraseña aleatoria con caracteres alfanuméricos y símbolos.
# Parámetros:
#   - longitud: Longitud de la contraseña (por defecto 8).
#   - cantidad: Cantidad de contraseñas a generar (por defecto 1).
# Respuesta: JSON con las contraseñas generadas.
###########
@app.route('/api/ContraseñaAleatoria', methods=['GET'])
def ContraseñaAleatoria():
    """
    Genera una contraseña aleatoria con caracteres alfanuméricos y símbolos.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
      - name: longitud
        in: query
        type: integer
        required: false
        default: 8
    responses:
      200:
        description: Contraseña aleatoria de 8 caracteres
        examples:
          application/json: {"cantidad":1,"contrasenas":{"contraseña_1":"ZKBl5OWO"},
          "error":false,"longitud":8,"status":200}
      400:
        description: Cantidad de contraseñas menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad debe ser mayor a 0.","status":400}
    """
    longitud = request.args.get('longitud', 8, type=int)
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001
            }), 400
    
    if longitud <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La longitud debe ser mayor a 0.',
            'code': 1002
            }), 400

    caracteres = (
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '0123456789'
        '!#$%&*-=+?'
    )

    contrasenas = {
        f"contraseña_{i+1}": ''.join(choices(caracteres, k=longitud))
        for i in range(cantidad)
    }

    return jsonify({
        'status': 200,
        'error': False,
        'contrasenas': contrasenas,
        'longitud': longitud,
        'cantidad': cantidad
    }), 200

### API ###
# Nombre: FechaAleatoria
# Tipo: GET
# Descripción: Genera una fecha aleatoria entre dos fechas dadas.
# Parámetros:
#   - fecha_inicial: Fecha inicial (por defecto 01/01/2000).
#   - fecha_final: Fecha final (por defecto la fecha actual).
#   - cantidad: Cantidad de fechas a generar (por defecto 1).
# Respuesta: JSON con la fecha aleatoria generada.
###########
@app.route('/api/FechaAleatoria', methods=['GET'])
def FechaAleatoria():
    """
    Genera una fecha aleatoria entre dos fechas dadas.
    ---
    parameters:
      - name: fecha_inicial
        in: query
        type: string
        required: false
        default: 01/01/2000
      - name: fecha_final
        in: query
        type: string
        required: false
        default: fecha actual
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Fecha aleatoria
        examples:
          application/json: {"cantidad":1,"error":false,
          "fechas_aleatorias":{"fecha_1":"12/01/2021"},"status":200}
      400:
        description: Formato de fecha inválido
        examples:
          application/json: {"code":1003,"error":true,
          "message":"Formato de fecha inválido. Usa DD/MM/YYYY.","status":400}
    """
    fecha_inicial_str = request.args.get('fecha_inicial', '01/01/2000')
    fecha_final_str = request.args.get(
        'fecha_final',
        datetime.today().strftime('%d/%m/%Y')
    )
    cantidad = request.args.get('cantidad', 1, type=int)

    try:
        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d/%m/%Y')
        fecha_final = datetime.strptime(fecha_final_str, '%d/%m/%Y')
    except ValueError:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Formato de fecha inválido. Usa DD/MM/YYYY.',
            'code': 1003
            }), 400

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001
            }), 400

    if fecha_inicial > fecha_final:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La fecha inicial no puede ser posterior a la fecha final.',
            'code': 1002
            }), 400

    delta = (fecha_final - fecha_inicial).days
    fechas_aleatorias = {
        f"fecha_{i+1}": (fecha_inicial + timedelta(days=randint(0, delta))).strftime('%d/%m/%Y')
        for i in range(cantidad)
    }

    return jsonify({
        'status': 200,
        'error': False,
        'fechas_aleatorias': fechas_aleatorias,
        'cantidad': cantidad
    }), 200

### API ###
# Nombre: HoraAleatoria
# Tipo: GET
# Descripción: Genera una hora aleatoria entre dos horas dadas.
# Parámetros:
#   - hora_inicial: Hora inicial (por defecto 00:00:00).
#   - hora_final: Hora final (por defecto 23:59:59).
#   - cantidad: Cantidad de horas a generar (por defecto 1).
# Respuesta: JSON con la hora aleatoria generada.
###########
@app.route('/api/HoraAleatoria', methods=['GET'])
def HoraAleatoria():
    """
    Genera una hora aleatoria entre dos horas dadas.
    ---
    parameters:
      - name: hora_inicial
        in: query
        type: string
        required: false
        default: 00:00:00
      - name: hora_final
        in: query
        type: string
        required: false
        default: '23:59:59'
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Hora aleatoria
        examples:
          application/json: {"cantidad":1,"error":false,
          "horas_aleatorias":{"hora_1":"05:00:30"},"status":200}
      400:
        description: Formato de hora inválido
        examples:
          application/json: {"code":1003,"error":true,
          "message":"Formato de hora inválido. Usa HH:MM:SS.","status":400}
    """
    hora_inicial_str = request.args.get('hora_inicial', '00:00:00')
    hora_final_str = request.args.get('hora_final', '23:59:59')
    cantidad = request.args.get('cantidad', 1, type=int)

    try:
        hora_inicial = datetime.strptime(hora_inicial_str, '%H:%M:%S').time()
        hora_final = datetime.strptime(hora_final_str, '%H:%M:%S').time()
    except ValueError:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Formato de hora inválido. Usa HH:MM:SS.',
            'code': 1003
            }), 400

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001
            }), 400

    if hora_inicial > hora_final:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La hora inicial no puede ser posterior a la hora final.',
            'code': 1002
            }), 400

    horas_aleatorias = {
        f"hora_{i+1}": (datetime.combine(datetime.today(), hora_inicial) +
                        timedelta(seconds=randint(0, (datetime.combine(datetime.today(), hora_final) - 
                        datetime.combine(datetime.today(), hora_inicial)).seconds))).time()
                        .strftime('%H:%M:%S')
        for i in range(cantidad)
    }

    return jsonify({
        'status': 200,
        'error': False,
        'horas_aleatorias': horas_aleatorias,
        'cantidad': cantidad
    }), 200

### API ###
# Nombre: ColorAleatorio
# Tipo: GET
# Descripción: Genera un color aleatorio en formato hexadecimal.
# Parámetros:
#   - cantidad: Cantidad de colores a generar (por defecto 1).
# Respuesta: JSON con los colores generados.
###########
@app.route('/api/ColorAleatorio', methods=['GET'])
def ColorAleatorio():
    """
    Genera un color aleatorio en formato hexadecimal.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Color hexadecimal aleatorio
        examples:
          application/json: {"cantidad":1,"colores":{"color_1":"#1e6b15"},
          "error":false,"status":200}
      400:
        description: Cantidad de colores menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a 0.',
            'code': 1001,
            }), 400

    colores = {
        f"color_{i+1}": '#{:02x}{:02x}{:02x}'.format(randint(0, 255), randint(0, 255), randint(0, 255))
        for i in range(cantidad)
    }

    return jsonify({
        'status': 200,
        'error': False,
        'colores': colores,
        'cantidad': cantidad
    })

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
