from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, jsonify
import os
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"

app = Flask(__name__)

@app.route('/operar_elite', methods=['POST', 'GET'])
def operacao():
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20) # Espera técnica de até 20 segundos
    try:
        driver.get("https://qxbroker.com/pt/login")
        
        # Espera o campo de e-mail aparecer de verdade
        email_field = wait.until(EC.presence_of_element_status((By.NAME, "email")))
        email_field.send_keys("clashofclansclgcv10@gmail.com")
        
        driver.find_element(By.NAME, "password").send_keys("Miguel02$$")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Espera o gráfico carregar
        time.sleep(15) 

        # Clica no botão de COMPRA (VERDE)
        driver.find_element(By.CLASS_NAME, "btn-call").click()

        return jsonify({"status": "Sucesso", "msg": "Operação de R$ 5 realizada!"})
    except Exception as e:
        return jsonify({"status": "Erro", "msg": "O site demorou a responder ou mudou o botão."})
    finally:
        driver.quit()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
