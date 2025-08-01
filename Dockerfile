FROM python:3.12-bullseye

EXPOSE 3000

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "app.py"]