FROM balenalib/raspberry-pi-debian:latest
MAINTAINER Franz Graf "code@locked.de"
RUN apt-get update
RUN apt-get install apt-utils
RUN apt-get install python3 python3-pip libusb-1.0-0 libudev0 pm-utils
RUN apt-get clean && apt-get autoremove
RUN curl -L http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb && \
    sudo dpkg -i brickd_linux_latest_armhf.deb && \
    rm brickd_linux_latest_armhf.deb
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
