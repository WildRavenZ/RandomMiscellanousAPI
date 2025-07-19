### DOCUMENTACIÓN ###
# Nombre: RandomMiscellaneousAPI.py
# Autor: Fernando Franco Zago
# Fecha: 19/07/2025
# Versión: 1.2.2
# Descripción: RandomMiscellaneousAPI es una API desarrollada con Flask que
#    permite generar diversos datos aleatorios útiles para pruebas, simulaciones,
#    juegos, educación o desarrollo de software. Entre sus funcionalidades se
#    incluyen la generación de números aleatorios, lanzamientos de moneda, selección
#    aleatoria de elementos desde listas, coordenadas geográficas, fechas,
#    contraseñas seguras, colores en formato hexadecimal y mucho más. La API es
#    altamente configurable y está diseñada para ofrecer respuestas claras,
#    estructuradas y listas para integrarse en sistemas frontend, scripts 
#    automatizados o entornos de desarrollo.
# Requisitos: pip install Flask, pip install flask-cors, pip install flasgger, pip install faker
# Librerías: Flask, jsonify, request, CORS, Swagger, Faker, randint, sample, uniform, choices, choice, datetime, timedelta
#####################

### LIBRERÍAS ###
# Instaladas
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from faker import Faker
# Nativas
from random import randint, sample, uniform, choices, choice
from datetime import datetime, timedelta
#################

app = Flask(__name__)
CORS(app)

# Configuración de Swagger
swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "RandomMiscellaneousAPI",
        "description": "RandomMiscellaneousAPI es una API desarrollada con Flask que permite generar diversos datos aleatorios útiles para pruebas, simulaciones, juegos, educación o desarrollo de software. Entre sus funcionalidades se incluyen la generación de números aleatorios, lanzamientos de moneda, selección aleatoria de elementos desde listas, coordenadas geográficas, fechas, contraseñas seguras, colores en formato hexadecimal y mucho más. La API es altamente configurable y está diseñada para ofrecer respuestas claras, estructuradas y listas para integrarse en sistemas frontend, scripts automatizados o entornos de desarrollo.",
        "version": "1.2.2",
        "contact": {
            "name": "Fernando Franco Zago"
        }
    },
    "host": "randommiscellanousapi.onrender.com",
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
        "fecha": "21/06/2025",
        "version": "1.2.0",
        "descripcion": "RandomMiscellaneousAPI es una API desarrollada con Flask que permite generar diversos datos aleatorios útiles para pruebas, simulaciones, juegos, educación o desarrollo de software. Entre sus funcionalidades se incluyen la generación de números aleatorios, lanzamientos de moneda, selección aleatoria de elementos desde listas, coordenadas geográficas, fechas, contraseñas seguras, colores en formato hexadecimal y mucho más. La API es altamente configurable y está diseñada para ofrecer respuestas claras, estructuradas y listas para integrarse en sistemas frontend, scripts automatizados o entornos de desarrollo.",
        "requisitos": ["pip install Flask", "pip install flask-cors", "pip install flasgger", "pip install faker"],
        "librerias": {
            "flask": ["Flask", "jsonify", "request"],
            "flask-cors": ["CORS"],
            "flasgger": ["Swagger"],
            "faker": ["Faker"],
            "random": ["randint", "sample", "uniform", "choices", "choice"],
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

    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'El límite de la cantidad debe ser menor a 100.',
            'code': 1000
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
        type: number
        format: float
        required: false
        default: 1.0
      - name: lim_superior
        in: query
        type: number
        format: float
        required: false
        default: 100.0
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

    if decimales < 0 or decimales > 10:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'El rango de decimales debe ser entre 0 y 10.',
            'code': 1002
        }), 400

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser mayor a cero.',
            'code': 1001
        }), 400
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'El límite de la cantidad debe ser menor a 100.',
            'code': 1000
        }), 400

    numeros = [f"{uniform(lim_inferior, lim_superior):.{decimales}f}" for _ in range(cantidad)]

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
          application/json: {"cartas_por_mano":1,"error":false,"manos":[{"mano_1":["10C"]}],
          "status":200,"total_cartas":1}
      400:
        description: No hay suficientes cartas en la baraja para repartir sin repetir.
        examples:
          application/json: {"code":1002,"error":true,
          "message":"No hay suficientes cartas en la baraja para repartir sin repetir.","status":400}
    """
    cartas_por_mano = request.args.get('cartas_por_mano', 1, type=int)
    manos = request.args.get('manos', 1, type=int)

    if cartas_por_mano <= 0 or manos <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Las cantidades de manos y cartas deben ser mayores a 0.',
            'code': 1001
            }), 400

    baraja = [
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"
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
    
    if lanzamientos > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de lanzamientos debe ser menor a 100.',
            'code': 1000
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
    
    if lanzamientos > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de lanzamientos debe ser menor a 100.',
            'code': 1000
            }), 400
    
    if dados <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de dados debe ser mayor a 0.',
            'code': 1002
            }), 400
    
    if dados > 10:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de dados debe ser menor a 10.',
            'code': 1000
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
# Nombre: NombreAleatorio
# Tipo: GET
# Descripción: Genera nombres aleatorios utilizando la librería Faker.
# Parámetros:
#   - cantidad: Cantidad de nombres a generar (por defecto 1).
# Respuesta: JSON con los nombres generados.
###########
@app.route('/api/NombreAleatorio', methods=['GET'])
def NombreAleatorio():
    """
    Genera nombres aleatorios utilizando la librería Faker.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un nombre aleatorio generado
        examples:
          application/json: {"cantidad":1,"error":false,"nombres":["John Doe"],"status":200}
      400:
        description: Cantidad de nombres menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de nombres debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de nombres debe ser mayor a 0.',
            'code': 1001
            }), 400
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de nombres debe ser menor a 100.',
            'code': 1000
            }), 400

    fake = Faker('es_MX')
    nombres = [fake.name() for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'nombres': nombres,
        'cantidad': cantidad
        }), 200

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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de decisiones debe ser menor a 100.',
            'code': 1000,
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de letras debe ser menor a 100.',
            'code': 1000
            }), 400

    letras = [chr(randint(65, 90)) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'letras': letras,
        'cantidad': cantidad
        }), 200

### API ###
# Nombre: CaracterAleatorio
# Tipo: GET
# Descripción: Genera caracteres aleatorios del conjunto ASCII imprimible.
# Parámetros:
#   - cantidad: Cantidad de caracteres a generar (por defecto 1).
# Respuesta: JSON con los caracteres generados.
###########
@app.route('/api/CaracterAleatorio', methods=['GET'])
def CaracterAleatorio():
    """
    Genera caracteres aleatorios del conjunto ASCII imprimible.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Un caracter aleatorio generado
        examples:
          application/json: {"cantidad":1,"error":false,"caracteres":["#"],"status":200}
      400:
        description: Cantidad de caracteres menor o igual a 0
        examples:
          application/json: {"code":1001,"error":true,
          "message":"La cantidad de caracteres debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de caracteres debe ser mayor a 0.',
            'code': 1001
            }), 400
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de caracteres debe ser menor a 100.',
            'code': 1000
            }), 400

    caracteres_validos = [chr(i) for i in range(32, 255) if i != 127]
    caracteres = [choice(caracteres_validos) for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'caracteres': caracteres,
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
# Nombre: EmojiAleatorio
# Tipo: GET
# Descripción: Genera un emoji aleatorio.
# Parámetros:
#   - cantidad: Cantidad de emojis a generar (por defecto 1).
# Respuesta: JSON con el emoji generado.
###########
@app.route('/api/EmojiAleatorio', methods=['GET'])
def EmojiAleatorio():
    """
    Genera uno o varios emojis aleatorios.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
    responses:
      200:
        description: Emojis aleatorios generados
        examples:
          application/json: {"cantidad":1,"error":false,"emojis":["😀"],"status":200}
      400:
        description: Cantidad inválida
        examples:
          application/json: {"code":1001,"error":true,"message":"La cantidad de emojis debe ser mayor a 0.","status":400}
    """
    cantidad = request.args.get('cantidad', 1, type=int)

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de emojis debe ser mayor a 0.',
            'code': 1001
        }), 400

    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de emojis debe ser menor a 100.',
            'code': 1000
        }), 400

    emoji_rangos = [
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F300, 0x1F5FF),  # Símbolos y pictogramas
        (0x1F680, 0x1F6FF),  # Transporte y mapas
        (0x1F1E6, 0x1F1FF),  # Banderas
        (0x1F900, 0x1F9FF),  # Símbolos suplementarios
        (0x1FA70, 0x1FAFF),  # Extensión de símbolos
    ]

    # Función interna para elegir un emoji válido
    def emoji_aleatorio():
        r = choice(emoji_rangos)
        return chr(choice(range(r[0], r[1] + 1)))

    emojis = [emoji_aleatorio() for _ in range(cantidad)]

    return jsonify({
        'status': 200,
        'error': False,
        'emojis': emojis,
        'cantidad': cantidad
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de coordenadas debe ser menor a 100.',
            'code': 1000,
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
# Nombre: PaisAleatorio
# Tipo: GET
# Descripción: Genera un país aleatorio de una lista predefinida.
# Parámetros:
#   - cantidad: Cantidad de países a generar (por defecto 1).
# Respuesta: JSON con los países generados.
###########
@app.route('/api/PaisAleatorio', methods=['GET'])
def PaisAleatorio():
    """
    Genera uno o varios países aleatorios, con opción de filtrar por continentes.
    ---
    parameters:
      - name: cantidad
        in: query
        type: integer
        required: false
        default: 1
      - name: continente
        in: query
        type: string
        required: false
        description: Puede ser uno o varios separados por coma.
    responses:
      200:
        description: Países aleatorios generados
      400:
        description: Petición inválida
    """
    cantidad = request.args.get('cantidad', 1, type=int)
    continente_str = request.args.get('continente', '').lower()

    if cantidad <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de países debe ser mayor a 0.',
            'code': 1001
        }), 400

    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad de países debe ser menor a 100.',
            'code': 1000
        }), 400

    paises_por_continente = {
        'america': ["Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canadá", "Chile", "Colombia", "Costa Rica",
            "Cuba", "Dominica", "Ecuador", "El Salvador", "Estados Unidos", "Granada", "Guatemala", "Guyana", "Haití",
            "Honduras", "Jamaica", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "República Dominicana",
            "San Cristóbal y Nieves", "Santa Lucía", "San Vicente y las Granadinas", "Surinam", "Trinidad y Tobago",
            "Uruguay", "Venezuela"],
        'europa': ["Alemania", "Andorra", "Austria", "Bélgica", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Croacia",
            "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Finlandia", "Francia", "Grecia", "Hungría",
            "Irlanda", "Islandia", "Italia", "Kosovo", "Letonia", "Liechtenstein", "Lituania", "Luxemburgo", "Malta",
            "Moldavia", "Mónaco", "Montenegro", "Noruega", "Países Bajos", "Polonia", "Portugal", "Reino Unido",
            "República Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania", "Vaticano"],
        'asia': ["Afganistán", "Arabia Saudita", "Armenia", "Azerbaiyán", "Bangladés", "Baréin", "Birmania", "Brunéi", "Bután",
            "Camboya", "Catar", "China", "Corea del Norte", "Corea del Sur", "Emiratos Árabes Unidos", "Filipinas",
            "Georgia", "India", "Indonesia", "Irak", "Irán", "Israel", "Japón", "Jordania", "Kazajistán", "Kirguistán",
            "Kuwait", "Laos", "Líbano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Omán", "Pakistán", "Singapur",
            "Siria", "Sri Lanka", "Tayikistán", "Tailandia", "Timor Oriental", "Turkmenistán", "Turquía", "Uzbekistán",
            "Vietnam", "Yemen"],
        'africa': ["Angola", "Argelia", "Benín", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerún", "Chad",
            "Comoras", "Congo", "Costa de Marfil", "Egipto", "Eritrea", "Esuatini", "Etiopía", "Gabón", "Gambia",
            "Ghana", "Guinea", "Guinea-Bisáu", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar",
            "Malaui", "Malí", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Namibia", "Níger", "Nigeria",
            "República Centroafricana", "República Democrática del Congo", "Ruanda", "Santo Tomé y Príncipe",
            "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Sudáfrica", "Sudán", "Sudán del Sur", "Tanzania",
            "Togo", "Túnez", "Uganda", "Yibuti", "Zambia", "Zimbabue"],
        'oceania': ["Australia", "Fiyi", "Islas Marshall", "Islas Salomón", "Kiribati", "Micronesia", "Nauru", "Nueva Zelanda",
            "Palaos", "Papúa Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]
    }

    pais_a_continente = {
        pais: continente
        for continente, paises in paises_por_continente.items()
        for pais in paises
    }

    if continente_str:
        continentes = [c.strip() for c in continente_str.split(',')]
        continentes_invalidos = [c for c in continentes if c not in paises_por_continente]

        if continentes_invalidos:
            return jsonify({
                'status': 400,
                'error': True,
                'message': f"Continente(s) no válido(s): {', '.join(continentes_invalidos)}. Usa america, europa, asia, africa, oceania.",
                'code': 1002
            }), 400

        paises_filtrados = sum((paises_por_continente[c] for c in continentes), [])
    else:
        paises_filtrados = list(pais_a_continente.keys())

    seleccionados = choices(paises_filtrados, k=cantidad)

    resultado = [
        {"pais": pais, "continente": pais_a_continente[pais]}
        for pais in seleccionados
    ]

    return jsonify({
        'status': 200,
        'error': False,
        'cantidad': cantidad,
        'paises': resultado
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000
            }), 400
    
    if longitud <= 0:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La longitud debe ser mayor a 0.',
            'code': 1002
            }), 400
    
    if longitud > 128:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La longitud debe ser menor a 128.',
            'code': 1000
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
    valores_str = request.args.get('valores_str')
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000
            }), 400
    
    if longitud <= 0 or longitud > 128:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La longitud debe ser mayor a 0 y menor a 128.',
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000
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
      - name: formato
        in: query
        type: string
        required: false
        default: '24h'
        enum: ['24h', '12h']
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
    formato = request.args.get('formato', '24h').lower()
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

    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000
        }), 400

    if hora_inicial > hora_final:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La hora inicial no puede ser posterior a la hora final.',
            'code': 1002
        }), 400

    if formato not in ['24h', '12h']:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'Formato no válido. Usa "12h" o "24h".',
            'code': 1004
        }), 400

    formato_strftime = '%I:%M:%S %p' if formato == '12h' else '%H:%M:%S'

    horas_aleatorias = {
        f"hora_{i+1}": (
            datetime.combine(datetime.today(), hora_inicial) +
            timedelta(seconds=randint(0, (datetime.combine(datetime.today(), hora_final) -
                                          datetime.combine(datetime.today(), hora_inicial)).seconds))
        ).strftime(formato_strftime) if formato == '12h' else
        (
            datetime.combine(datetime.today(), hora_inicial) +
            timedelta(seconds=randint(0, (datetime.combine(datetime.today(), hora_final) -
                                          datetime.combine(datetime.today(), hora_inicial)).seconds))
        ).strftime(formato_strftime)
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
    
    if cantidad > 100:
        return jsonify({
            'status': 400,
            'error': True,
            'message': 'La cantidad debe ser menor a 100.',
            'code': 1000,
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
    app.run()
