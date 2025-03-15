FROM python:3.9

WORKDIR /app

COPY web_app.py .
COPY style.css .

RUN pip install flask redis

EXPOSE 8081

CMD ["python", "web_app.py"]


