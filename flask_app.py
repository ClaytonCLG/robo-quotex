from flask import Flask, jsonify
from pyquotex import Quotex
import os

app = Flask(__name__)

@app.route('/operar_elite', methods=['POST', 'GET'])
def operacao():
    email = "clashofclansclgcv10@gmail.com"
    senha = "Miguel02$$"
    client = Quotex(email=email, password=senha)

    if client.connect():
        # ABRE COMPRA DE R$ 5
        sucesso, erro = client.open_order("EURUSD", 5, "call", 1)
        if sucesso:
            return jsonify({"status": "Sucesso", "mensagem": "ORDEM EXECUTADA!"})
        return jsonify({"status": "Erro", "mensagem": str(erro)})
    return jsonify({"status": "Erro", "mensagem": "Falha no login"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  
