<<<<<<< HEAD
FROM python:3.11-slim
=======
FROM python:3.11-slim
>>>>>>> 2c83444a3b1560d3b174cb200c57ef28c3e4e8bd

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
>>>>>>> 2c83444a3b1560d3b174cb200c57ef28c3e4e8bd
