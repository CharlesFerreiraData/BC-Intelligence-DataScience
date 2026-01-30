FROM python:3.11-slim

# Instala Java e ferramentas de sistema para o PySpark
RUN apt-get update && apt-get install -y \
    default-jre \
    procps \
    && apt-get clean

WORKDIR /app

# Instala as bibliotecas do projeto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Comando para iniciar a API automaticamente
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]