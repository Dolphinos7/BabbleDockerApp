FROM python:alpine3.11
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["flask", "run", "--host=0.0.0.0"]
