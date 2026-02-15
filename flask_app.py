from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask import Flask, jsonify
import os
import time

# --- 1. CONFIGURAÇÃO DO NAVEGADOR LEVE ---
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium" # Caminho do navegador leve

app = Flask(__name__)

@app.route('/operar_elite', methods=['POST', 'GET'])
def operacao():
    # Seus dados de acesso
    email_user = "clashofclansclgcv10@gmail.com"
    senha_user = "Miguel02$$"
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # --- 2. LOGIN NA QUOTEX ---
        driver.get("https://qxbroker.com/pt/login")
        time.sleep(5) # Espera o site carregar
        
        # Preenche E-mail e Senha
        driver.find_element(By.NAME, "email").send_keys(email_user)
        driver.find_element(By.NAME, "password").send_keys(senha_user + Keys.ENTER)
        time.sleep(10) # Espera o login e o gráfico carregarem
        
        # --- 3. CONFIGURAR VALOR E FAZER ENTRADA ---
        # (Lógica simplificada para encontrar os botões de Valor e Compra)
        # 1. Muda o valor para R$ 5
        campo_valor = driver.find_element(By.CSS_SELECTOR, ".input-control__input") 
        campo_valor.clear()
        campo_valor.send_keys("5")
        
        # 2. Clica no botão VERDE (CALL/COMPRA)
        botao_compra = driver.find_element(By.CLASS_NAME, "btn-call") 
        botao_compra.click()

        return jsonify({
            "status": "Sucesso", 
            "mensagem": "ORDEM DE R$ 5,00 ENVIADA PELO NAVEGADOR!",
            "par": "EURUSD"
        })

    except Exception as e:
        return jsonify({"status": "Erro", "mensagem": str(e)})
    
    finally:
        driver.quit() # Fecha para não travar o servidor

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
