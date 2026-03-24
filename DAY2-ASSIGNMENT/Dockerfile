FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

COPY api_backend.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "api_backend:app", "--reload"]