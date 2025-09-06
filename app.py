from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from datetime import datetime  # ✅ Import necesario

app = Flask(__name__)
CORS(app)

# Configura tu clave de API de Gemini
genai.configure(api_key="AIzaSyCL5682QZsS5e25NvTfs4QbtFz1r7SAkQU")

# Rutas para páginas HTML
@app.route("/")
def index():
    return render_template("index.html", year=datetime.now().year)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html", year=datetime.now().year)

@app.route('/proyecto')
def proyecto():
    return render_template('proyecto.html')  # tu nueva hoja HTML

@app.route('/ichat')
def ichat():
     return render_template('ichat.html', year=datetime.now().year)


# Ruta para la API de chat
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "No recibí ningún mensaje."}), 400

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"Error con Gemini: {e}")
        return jsonify({"reply": "Ocurrió un error con el servicio de IA de Gemini."}), 500

if __name__ == "__main__":
    app.run(debug=True)
