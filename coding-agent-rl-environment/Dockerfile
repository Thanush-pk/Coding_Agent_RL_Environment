FROM python:3.11-slim

WORKDIR /workspace

ENV PYTHONPATH=/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY tests ./tests
COPY task ./task

CMD ["pytest", "-q"]