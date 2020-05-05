FROM python:alpine3.11
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN apk add curl
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=5s --timeout=60s CMD curl -f http://localhost:5000/api/blabs || exit 1
