FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=8080
# App should read: DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, BG_COLOR
EXPOSE 8080
CMD ["python", "app.py"]
