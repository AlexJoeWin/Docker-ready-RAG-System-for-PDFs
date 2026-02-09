FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpoppler-cpp-dev && rm -rf /var/lib/apt/lists/*

COPY . .

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
