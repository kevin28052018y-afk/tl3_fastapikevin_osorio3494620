FROM python:3.11-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# El backend (FastAPI) usa el puerto 8000, por eso Django corre en el 8001

CMD gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:8001}