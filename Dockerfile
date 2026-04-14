FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV BOT_TOKEN=8688557974:AAHvHzYWINrRDfGnKymO2gfUdP01J7R3IjQ
ENV CHANNEL_ID=-1003120043320
ENV YOUR_WEBSITE=www.animethic.xyz
ENV YOUR_CHANNEL=@animethic2

CMD ["python", "main.py"]
