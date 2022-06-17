FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -U -r requirements.txt

COPY . .

ENV FLASK_ENV=develop
ENV FLASK_APP=webapp

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
