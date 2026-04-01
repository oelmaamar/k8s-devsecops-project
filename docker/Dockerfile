FROM python:3.10-slim

WORKDIR /app

COPY app/app.py /app/app.py

RUN pip install --no-cache-dir --upgrade pip setuptools wheel==0.46.2
RUN pip install flask


EXPOSE 5000

CMD ["python", "app.py"]
