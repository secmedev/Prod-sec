FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        make \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        libjpeg62-turbo-dev \
        libfreetype6-dev \
        libopenjp2-7-dev \
        libtiff-dev \
        libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --upgrade "pip<24" "setuptools<70" wheel

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/app.py"]
