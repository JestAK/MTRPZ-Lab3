FROM python:3.12-slim
WORKDIR /app

COPY ../../requirements/backend.in ./
RUN pip install --no-cache-dir -r backend.in

COPY . ./../spaceship ./spaceship
COPY ../../build ./build

EXPOSE 8080

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0", "--port", "8080"]