FROM python:3.10.12-alpine

WORKDIR /attacker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY attack.py .

CMD ["tail", "-f", "/dev/null"]
