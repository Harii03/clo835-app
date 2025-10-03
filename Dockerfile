# --- app/Dockerfile ---
FROM python:3.11-slim

# Avoid __pycache__ files & get real-time logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) Install Python deps first (build cache friendly)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copy the rest of the app (includes templates/ and static/)
COPY . .

# app listens on 8080
ENV PORT=8080
EXPOSE 8080

# Run the flask app
CMD ["python", "app.py"]
