FROM python:3.12.4

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0"]
