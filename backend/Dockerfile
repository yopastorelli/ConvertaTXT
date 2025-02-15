FROM python:3.9-slim

WORKDIR /app

# Copiar e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Definir variáveis de ambiente para facilitar a configuração
ENV DATABASE_URL="postgresql+psycopg2://user:password@db/converta_txt"
ENV REDIS_URL="redis://redis:6379/0"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
