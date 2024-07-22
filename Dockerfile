FROM python:3.12
WORKDIR /app
RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/local.txt
COPY . /app/