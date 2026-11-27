FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Genera el modelo en el build
RUN mkdir -p model && python train.py

EXPOSE 8080

# Usa el puerto que Railway asigna; en local, 8080
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]