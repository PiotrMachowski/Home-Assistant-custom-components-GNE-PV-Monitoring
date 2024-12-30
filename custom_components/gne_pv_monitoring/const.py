import datetime

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (UnitOfElectricCurrent, UnitOfElectricPotential, UnitOfEnergy, UnitOfPower,
                                 UnitOfTemperature, Platform)
from homeassistant.helpers.entity import EntityCategory

NAME = "GNE PV Monitoring"
DOMAIN = "gne_pv_monitoring"

# Icons
ICON = "mdi:solar-panel"

# Platforms
PLATFORMS = [Platform.SENSOR]
SCAN_INTERVAL = datetime.timedelta(minutes=5, seconds=1)

# Configuration and options
CONF_APP_ID = "app_id"
CONF_APP_SECRET = "app_secret"
CONF_BEEHIVE_ID = "beehive_id"

# Defaults
DEFAULT_NAME = DOMAIN

# API
URL = "http://newapi.gnetek.com/trdapp/queryBeehiveHoneybees"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
MIN_TIME_BETWEEN_CALLS = datetime.timedelta(minutes=5)
PARAMETERS = {
    "inVoltage1": {
        "unit": UnitOfElectricPotential.VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:lightning-bolt-circle",
        "entity_category": None
    },
    "inCurrent1": {
        "unit": UnitOfElectricCurrent.AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-dc",
        "entity_category": None
    },
    "power1": {
        "unit": UnitOfPower.WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:flash",
        "entity_category": None
    },
    "outVoltage": {
        "unit": UnitOfElectricPotential.VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:lightning-bolt-circle",
        "entity_category": None
    },
    "outCurrent": {
        "unit": UnitOfElectricCurrent.AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:current-dc",
        "entity_category": None
    },
    "dailyEnergy": {
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:solar-power",
        "entity_category": None
    },
    "temperature": {
        "unit": UnitOfTemperature.CELSIUS,
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:thermometer",
        "entity_category": None
    },
    "transTime": {
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:clock-outline",
        "entity_category": EntityCategory.DIAGNOSTIC
    },
    "warnCode": {
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:alert",
        "entity_category": EntityCategory.DIAGNOSTIC
    },
    "status": {
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:solar-panel",
        "entity_category": EntityCategory.DIAGNOSTIC
    }
}
