FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y --no-install-recommends libjpeg62-turbo-dev zlib1g-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 53

CMD ["python", "PythonApplication1/PythonApplication1.py"]
