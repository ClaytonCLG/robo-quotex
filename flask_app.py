from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Roda sem janela (obrigatório no Render)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://qxbroker.com/pt/login")

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
        status, erro = client.open_order("EURUSD", 5, "call", 1)
        if status:
            return jsonify({"status": "Sucesso", "mensagem": "ORDEM ABERTA!"})
        return jsonify({"status": "Erro", "mensagem": str(erro)})
    return jsonify({"status": "Erro", "mensagem": "Falha no login"})

if __name__ == "__main__":
    # O Render usa a porta automática ou a 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
