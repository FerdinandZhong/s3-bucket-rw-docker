FROM python:3.7-stretch

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD [ "-v" ]