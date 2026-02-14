FROM python:3.9-slim

# Instala apenas o necessário para o navegador rodar
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "flask_app:app", "--bind", "0.0.0.0:10000"]
