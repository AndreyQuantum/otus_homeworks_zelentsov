FROM python:3.9.13-bullseye
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x startup.sh