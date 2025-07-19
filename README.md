# 🧪 RandomMiscellaneousAPI [1.2.2]

![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.0-lightgrey?logo=flask)
![Flask](https://img.shields.io/badge/FlaskCORS-5.0.1-lightgrey?logo=flask)
![Flasgger](https://img.shields.io/badge/Flasgger-0.9.7.1-blueviolet?logo=swagger&logoColor=white)
![Deploy](https://img.shields.io/badge/Render-Live-brightgreen)

RandomMiscellaneousAPI es una API desarrollada con Flask que permite generar diversos datos aleatorios útiles para pruebas, simulaciones, juegos, educación o desarrollo de software. Entre sus funcionalidades se incluyen la generación de números aleatorios, lanzamientos de moneda, selección aleatoria de elementos desde listas, coordenadas geográficas, fechas, contraseñas seguras, colores en formato hexadecimal y mucho más. La API es altamente configurable y está diseñada para ofrecer respuestas claras, estructuradas y listas para integrarse en sistemas frontend, scripts automatizados o entornos de desarrollo.

---

## 📃 Documentación en línea

👉 [https://randommiscellanousapi.onrender.com/apidocs/#/](https://randommiscellanousapi.onrender.com/apidocs/#/)

## ⚙️ Tecnologías usadas

- 🐍 Python 3.11.9 (Lógica para las APIs)
- 🌐 Flask 3.1.0 (Framework)
- ⚙ Flask-cors 5.0.1 (CORS)
- 📃 Flasgger 0.9.7.1 (Documentación)
- ☁️ Render.com (Hosting gratuito)

## 📚 Librerías usadas
### Instaladas:
- flask: `Flask`, `jsonify`, `request`.
- flask_cors: `CORS`.
- flasgger: `Swagger`.
- faker: `Faker`.
### Nativas:
- random: `randint`, `sample`, `uniform`, `choices`, `choice`.
- datetime: `datetime`, `timedelta`.

## 💻 Descripción de Endpoints
#### Endpoints totales: 19
Siendo la URL base: https://randommiscellanousapi.onrender.com/:
- 🃏 [api/BarajaAleatoria](https://randommiscellanousapi.onrender.com/api/BarajaAleatoria) - Genera manos de cartas aleatorias de una baraja inglesa.
- 🔢 [api/BinarioAleatorio](https://randommiscellanousapi.onrender.com/api/BinarioAleatorio) - Genera un número binario aleatorio de una longitud específica.
- 🔤 [api/CaracterAleatorio](https://randommiscellanousapi.onrender.com/api/CaracterAleatorio) - Genera un caracter aleatorio del conjunto ASCII.
- 🎨 [api/ColorAleatorio](https://randommiscellanousapi.onrender.com/api/ColorAleatorio) - Genera un color aleatorio en formato hexadecimal.
- 🔤 [api/ContraseñaAleatoria](https://randommiscellanousapi.onrender.com/api/ContraseñaAleatoria) - Genera una contraseña aleatoria con caracteres alfanuméricos y símbolos.
- 🌎 [api/CoordenadaAleatoria](https://randommiscellanousapi.onrender.com/api/CoordenadaAleatoria) - Genera coordenadas geográficas aleatorias con latitud y longitud.
- 💡 [api/DecisionAleatoria](https://randommiscellanousapi.onrender.com/api/DecisionAleatoria) - Genera decisiones aleatorias entre Si y No.
- 😁 [api/EmojiAleatorio](https://randommiscellanousapi.onrender.com/api/EmojiAleatorio) - Genera un emoji de manera aleatoria.
- 📆 [api/FechaAleatoria](https://randommiscellanousapi.onrender.com/api/FechaAleatoria) - Genera una fecha aleatoria entre dos fechas dadas.
- 🕒 [api/HoraAleatoria](https://randommiscellanousapi.onrender.com/api/HoraAleatoria) - Genera una hora aleatoria entre dos horas dadas.
- 🎲 [api/LanzamientosDado](https://randommiscellanousapi.onrender.com/api/LanzamientosDado) - Genera lanzamientos de un dado con resultados entre 1 y 6.
- 🟡 [api/LanzamientosMoneda](https://randommiscellanousapi.onrender.com/api/LanzamientosMoneda) - Genera lanzamientos de moneda con resultados entre cara o cruz.
- 🅰 [api/LetraAleatoria](https://randommiscellanousapi.onrender.com/api/LetraAleatoria) - Genera letras aleatorias del alfabeto inglés entre A y Z.
- 👨‍👦 [api/NombreAleatorio](https://randommiscellanousapi.onrender.com/api/NombreAleatorio) - Genera el nombre de una persona aleatoria.
- 🔢 [api/NumAleatorio](https://randommiscellanousapi.onrender.com/api/NumAleatorio) - Genera números aleatorios entre un límite inferior y superior.
- 🔢 [api/NumDecimalAleatorio](https://randommiscellanousapi.onrender.com/api/NumDecimalAleatorio) - Genera números decimales aleatorios entre un límite inferior y superior.
- 🌎 [api/PaisAleatorio](https://randommiscellanousapi.onrender.com/api/PaisAleatorio) - Genera un país de manera aleatoria.
- ✋ [api/PiedraPapelTijera](https://randommiscellanousapi.onrender.com/api/PiedraPapelTijera) - Genera una decisión aleatoria entre piedra, papel o tijera.
- 🧾 [api/SeleccionAleatoria](https://randommiscellanousapi.onrender.com/api/SeleccionAleatoria?valores=rojo,verde,azul) - Selecciona aleatoriamente elementos de una lista dada.

Para información más detallada sobre el funcionamiento de los endpoints, consulta la [documentación en línea](https://randommiscellanousapi.onrender.com/apidocs/#/).

## ⚖ Licencia
Este proyecto está bajo la licencia [MIT](LICENSE).

## 📈 Estado del proyecto
### 1.2.2 (Versión actual):
- Arreglado error relacionado con la documentación Swagger.
### 1.2.1
- La API de `HoraAleatoria` puede devolver los resultados en formatos de 24 o 12 horas si se usa el argumento: `formato=12h`.
- La API de `PaisAleatorio` ahora devuelve el continente de cada país y funciona haciendo filtro de dicho continente. Por ejemplo, al agregar el argumento: `continente=asia,europa` realizará la selección aleatoria de esos continentes. Si se deja vacío, funcionará de manera normal.
- Cambios en la documentación y el README.
### 1.2.0:
- Se agregaron 4 nuevas funciones: `NombreAleatorio`, `PaisAleatorio`, `CaracterAleatorio` y `EmojiAleatorio`.
- Se arreglaron errores varios en el manejo de las sulicitudes.
- La API usa la librería `faker` para generación de nombres.
- Cambios en la documentación y el README.
### 1.1.0:
- Primera versión de API compatible con [Random Miscellaneous Web](https://wildravenz.github.io/Random-Miscellaneous-Web/).
- Se implementaron ciertas limitaciones en los consumos de la API para no sobresaturar la memoria del servidor. Ahora, las cantidades de generaciones que se puede realizar por API son de un máximo de 100.
- Otras variables de entrada en las APIs también fueron limitadas variadamente.
### 1.0.3:
- Se modificó la función de `NumDecimalAleatorio` para ser más útil.
### 1.0.2:
- Se agregó `flask-cors` para un consumo de API más permisivo en sitios web https.
- Se cambió la documentación.
### 1.0.1:
- Se arreglaron errores relacionados al consumo de la API de `BarajaAleatoria`.
### 1.0.0:
- API creada y hosteada en línea.

## 🙋‍♂️ Autores y contribuidores
- Fernando Franco Zago (Autor) [Github](https://github.com/WildRavenZ) y [LinkedIn](https://www.linkedin.com/in/fernando-franco-zago-066840313/).

#### *Actualizado al 19/07/2025*
