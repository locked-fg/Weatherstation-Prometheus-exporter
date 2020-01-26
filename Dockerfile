FROM balenalib/raspberry-pi-alpine:latest
MAINTAINER Franz Graf "code@locked.de"
RUN apk update && \
    apk add python3 && \
    pip3 install --upgrade pip && \
    pip3 install wheel && \
    rm rm -rf /root/.cache
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app.py /app/app.py
ENV FLASK_APP=app.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
