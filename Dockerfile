FROM docker.io/python:3.11-alpine
WORKDIR /bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot.py .
CMD python bot.py
