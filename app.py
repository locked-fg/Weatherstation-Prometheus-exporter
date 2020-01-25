from flask import Flask, request
import logging
from tinkerforge.bricklet_ambient_light import AmbientLight
from tinkerforge.bricklet_barometer import Barometer
from tinkerforge.bricklet_humidity import Humidity
from tinkerforge.bricklet_temperature import Temperature
from tinkerforge.ip_connection import IPConnection

app = Flask(__name__)
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Weatherstation')

#HOST = "localhost"
HOST = "raspberrypi-outside"
PORT = 4223

AMBIENT_UID = "jzj"
BAROMETER_UID = "FbW"
HUMIDITY_UID = "hRd"
TEMPERATURE_UID = "dXC"

@app.route("/")
def data():
    logger.setLevel(logging.INFO)
    out = []

    try:
        ipcon = IPConnection()
        ipcon.connect(HOST, PORT)

        out.append("weather_ambient_light_lux {}".format(get_light(ipcon)))
        out.append("weather_air_pressur_mbar {}".format(get_barometer(ipcon)))
        out.append("weather_humidity_percent {}".format(get_humidity(ipcon)))
        out.append("weather_temperature_degrees_celsius {}".format(get_temperature(ipcon)))

        ipcon.disconnect()
    except Exception as e:
        logger.error(e)
        return e
    return "\n".join(out)


def get_temperature(ipcon):
    t = Temperature(TEMPERATURE_UID, ipcon)  # Create device object
    return t.get_temperature() / 100.0


def get_humidity(ipcon):
    h = Humidity(HUMIDITY_UID, ipcon)  # Create device object
    return h.get_humidity() / 10.0


def get_barometer(ipcon):
    b = Barometer(BAROMETER_UID, ipcon)
    return b.get_air_pressure()/1000


def get_light(ipcon):
    al = AmbientLight(AMBIENT_UID, ipcon)
    return al.get_illuminance() / 10.0


if __name__ == "__main__":
    app.run()
