FROM python:3.12-slim
WORKDIR /app

COPY . ./../spaceship ./spaceship
COPY ../../build ./build

COPY ../../requirements/backend.in ./
RUN pip install --no-cache-dir -r backend.in

EXPOSE 8000

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0", "--port", "8080"]