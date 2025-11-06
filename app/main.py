from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello World, Flask API is running!"})

@app.route('/health-check', methods=['GET'])
def health():
    return jsonify({"status": "OK"})

@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    return jsonify({"message": f"Olá, {name}! Seja bem-vindo à API Flask."})

@app.route('/echo', methods=['POST'])
def echo_data():
    data = request.get_json()  # lê o corpo da requisição em JSON
    return jsonify({
        "received_data": data,
        "message": "Dados recebidos com sucesso!"
    })

if __name__ == '__main__':
    app.run(debug=True)
