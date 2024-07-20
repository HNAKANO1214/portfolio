FROM python:3.12
WORKDIR /app
COPY config/requirements/ /app/config/requirements/
RUN pip install --no-cache-dir -r config/requirements/local.txt
COPY . /app/