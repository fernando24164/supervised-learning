FROM python:3.7.4-slim
ADD ./webapp /app/webapp
ADD ./data /data
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /app/webapp
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]
