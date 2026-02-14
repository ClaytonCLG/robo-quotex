from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, jsonify
import os
import time

# --- 1. CONFIGURAÇÃO DO NAVEGADOR (CHROME) ---
options = Options()
options.add_argument("--headless")  # Obrigatório para rodar no Render sem tela
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome" # Local do Chrome no Docker

app = Flask(__name__)

@app.route('/operar_elite', methods=['POST', 'GET'])
def operacao():
    # Dados da sua conta
    email_user = "clashofclansclgcv10@gmail.com"
    senha_user = "Miguel02$$"
    
    # Inicia o navegador
    driver = webdriver.Chrome(options=options)
    
    try:
        # --- 2. LOGIN NA QUOTEX ---
        driver.get("https://qxbroker.com/pt/login")
        time.sleep(5) # Espera o site carregar
        
        # O robô procura os campos e preenche (exemplo de lógica)
        # driver.find_element(By.NAME, "email").send_keys(email_user)
        # driver.find_element(By.NAME, "password").send_keys(senha_user)
        
        # --- 3. COMANDO DA OPERAÇÃO ---
        # Aqui enviamos a ordem de R$ 5,00
        # Por enquanto, ele apenas confirma que acessou o navegador com sucesso
        
        return jsonify({
            "status": "Sucesso",
            "mensagem": "Navegador Chrome iniciado no Render!",
            "conta": email_user,
            "valor": "R$ 5,00"
        })

    except Exception as e:
        return jsonify({"status": "Erro", "mensagem": str(e)})
    
    finally:
        driver.quit() # Fecha o navegador para não gastar memória

if __name__ == "__main__":
    # Porta automática do Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
