import datetime

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT, ENERGY_WATT_HOUR, POWER_WATT, \
    TEMP_CELSIUS

NAME = "GNE PV Monitoring"
DOMAIN = "gne_pv_monitoring"

# Icons
ICON = "mdi:solar-panel"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Configuration and options
CONF_APP_ID = "app_id"
CONF_APP_SECRET = "app_secret"
CONF_BEEHIVE_ID = "beehive_id"

# Defaults
DEFAULT_NAME = DOMAIN

# API
URL = "http://newapi.gnetek.com/trdapp/queryBeehiveHoneybees"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
MIN_TIME_BETWEEN_CALLS = datetime.timedelta(minutes=10)
PARAMETERS = {
    "inVoltage1": {
        "unit": ELECTRIC_POTENTIAL_VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "inCurrent1": {
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "power1": {
        "unit": POWER_WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "outVoltage": {
        "unit": ELECTRIC_POTENTIAL_VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "outCurrent": {
        "unit": ELECTRIC_CURRENT_AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    "dailyEnergy": {
        "unit": ENERGY_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
    },
    "temperature": {
        "unit": TEMP_CELSIUS,
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
    }
}
