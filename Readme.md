# Project for polling the sensor data and expose it to prometheus

# Prepare Tinkerforge bricks
https://www.tinkerforge.com/de/doc/Embedded/Raspberry_Pi.html
```bash
sudo apt-get install libusb-1.0-0 libudev0 pm-utils
wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
sudo dpkg -i brickd_linux_latest_armhf.deb
```
Updates (later)
```bash
wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
sudo dpkg -i brickd_linux_latest_armhf.deb
```


# Install Weatherstation
Install Pyton and dependencies
```bash
sudo apt install python3 sqlite python3-setuptools
sudo easy_install3 pip
pip install tinkerforge
```
Download weatherstation
```bash
cd /home/pi
git clone https://github.com/locked-fg/Weatherstation-Python.git Weatherstation
```

Optional: Restore data at `~/Weatherstation/data/sensors.db` 

Add entries to crontab 
```
* * * * * ~/Weatherstation/temperature.py
* * * * * ~/Weatherstation/humidity.py
* * * * * ~/Weatherstation/ambientlight.py
* * * * * ~/Weatherstation/barometer.py
* * * * * ~/Weatherstation/startSqlite.sh
* * * * * curl -T ~/Weatherstation/data/series.json ftp://[hostname] --user ftplogin:password
* * * * * curl -T ~/Weatherstation/data/table.json  ftp://[hostname] --user ftplogin:password
```