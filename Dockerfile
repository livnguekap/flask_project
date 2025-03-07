FROM python:3.8.16-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["app.py"]