import subprocess
import sys

# FORÇA A INSTALAÇÃO DA QUOTEX SE ELA NÃO EXISTIR
try:
    from pyquotex import Quotex
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyquotex"])
    from pyquotex import Quotex

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/operar_elite', methods=['POST', 'GET'])
def operacao():
    email = "clashofclansclgcv10@gmail.com"
    senha = "Miguel02$$"
    client = Quotex(email=email, password=senha)
    
    if client.connect():
        status, erro = client.open_order("EURUSD", 5, "call", 1)
        if status:
            return jsonify({"status": "Sucesso", "mensagem": "ORDEM ABERTA!"})
        return jsonify({"status": "Erro", "mensagem": str(erro)})
    return jsonify({"status": "Erro", "mensagem": "Falha no login"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  
