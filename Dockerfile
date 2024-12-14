
FROM python:3.12.7-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt





FROM python:3.12.7-slim

RUN useradd -m myuser
USER myuser

WORKDIR /app

COPY --from=builder /root/.local /home/myuser/.local
COPY --from=builder /root/.local/bin /home/myuser/.local/bin
ENV PATH=/home/myuser/.local/bin:$PATH
COPY src/ .

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
