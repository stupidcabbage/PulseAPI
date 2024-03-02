FROM python:3.12.1-alpine3.19 AS builder

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry==1.8.1 \
    && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

FROM python:3.12.1-alpine3.19

WORKDIR /app

COPY --from=builder requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY src/ .


ENV POSTGRES_USERNAME="prodtest"
ENV POSTGRES_PASSWORD="prodtest"
ENV POSTGRES_DATABASE="prodtest"
ENV POSTGRES_HOST="localhost"
ENV POSTGRES_PORT=5432
ENV SECRET_KEY="8Zz5tw0Ionm3XPZZfN0NOml3z9FMfmpgXwovR9fp6ryDIoGRM8EPHAB6iHsc0fb"
ENV SERVER_ADRESS="localhost"
ENV SERVER_PORT=8000

CMD ["sh", "-c", "exec alembic upgrade head; exec python3 -m uvicorn main:app --host=0.0.0.0 --port=$SERVER_PORT"]
