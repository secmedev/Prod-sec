FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y \
        gcc \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/app.py"]
