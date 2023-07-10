FROM python:3.11

WORKDIR "/app"

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

ENV REDIS_HOST=redis-server

CMD ["python", "main.py"]