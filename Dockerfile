FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY model.py /app
COPY requirements.txt /app
COPY data_daily.csv /app

RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["python", "model.py"]
