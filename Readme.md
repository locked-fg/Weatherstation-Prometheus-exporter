# Project for polling the sensor data and expose it to prometheus

Brick Daemon must be installed on the host: 
https://www.tinkerforge.com/de/doc/Software/Brickd_Install_Linux.html#brickd-install-linux

## Build
```
docker build -t locked_fg/weatherstation_prometheus_exporter:latest .
```

## Run
```
docker container stop weatherstation_prometheus_exporter
docker container rm weatherstation_prometheus_exporter
docker run -d -p 5000:5000 \
 -e BRICKD_HOST=`hostname` \
 --restart=always \
 --name weatherstation_prometheus_exporter locked_fg/weatherstation_prometheus_exporter:latest
```

## TODO
change to base image `raspberry-pi-alpine`