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
    # Espera técnica de até 30 segundos
    wait = WebDriverWait(driver, 30) 
    try:
        driver.get("https://qxbroker.com/pt/login")
        
        # ESPERA O CAMPO APARECER (Resolve o erro da imagem 34908.jpg)
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_field.send_keys("clashofclansclgcv10@gmail.com")
        
        driver.find_element(By.NAME, "password").send_keys("Miguel02$$")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Espera o gráfico carregar para dar a entrada de R$ 5
        time.sleep(20) 
        driver.find_element(By.CLASS_NAME, "btn-call").click()

        return jsonify({"status": "Sucesso", "msg": "Ordem de R$ 5 enviada!"})
    except Exception as e:
        return jsonify({"status": "Erro", "msg": str(e)})
    finally:
        driver.quit()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
