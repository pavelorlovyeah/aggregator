FROM python:3.9-slim

RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

COPY pyproject.toml /app
RUN pip install .

COPY /src/aggregator /app

ENV VABUS_URL=http://host:port
ENV STORAGE_TYPE=postgres
ENV AGGREGATION_INTERVAL=60

CMD ["python", "/app/main.py"]