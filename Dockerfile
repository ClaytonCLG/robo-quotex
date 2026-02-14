FROM python:3.9

# Instala o Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y google-chrome-stable

# Copia seu código
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "flask_app:app", "--bind", "0.0.0.0:10000"]
