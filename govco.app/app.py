import capturas
import detecciones
import tldextract
import os
import cv2
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detectar_objetos():
    input = [x for x in request.form.values()]
    url = input[0]
    print(f"Pagina a analizar: {url}")
    
    # Se toma la captura de pantalla del sitio y se almacena en una carpeta de la aplicacion
    capturas.obtener_captura(url)

    extracted = tldextract.extract(url)
    dominio = extracted.domain
    directorio_script = os.path.dirname(__file__)
    
    # Imagen sobre la cual se detectaran los objetos
    ruta_img_analizar = os.path.join(directorio_script, 'capturas', dominio + ".png")
    imagen = cv2.imread(ruta_img_analizar)
    alto, ancho, canales = imagen.shape
    detectados, no_detectados, ruta_img = detecciones.detectar(ruta_img_analizar, dominio, ancho, alto)
    return render_template('detecciones.html', detectados=detectados, no_detectados=no_detectados, img=ruta_img, url=url)

if __name__ == '__main__':
    app.run(debug=True)