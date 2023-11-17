FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh","entrypoint.sh"]