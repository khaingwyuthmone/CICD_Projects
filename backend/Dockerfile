FROM python:3.8-slim

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /backend/

EXPOSE 5000

CMD [ "python", "-m", "main" ]