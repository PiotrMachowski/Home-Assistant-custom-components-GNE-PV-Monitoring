from homeassistant.components.sensor import ENTITY_ID_FORMAT, SensorEntity
from homeassistant.helpers.entity import async_generate_entity_id

from . import GnePVMonitoringDataUpdateCoordinator
from .const import (DEFAULT_NAME, DOMAIN, PARAMETERS)
from .entity import GnePVMonitoringEntity


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator: GnePVMonitoringDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    data = coordinator.data
    entities = []
    for mac_id in data:
        for parameter in PARAMETERS:
            entity_id = async_generate_entity_id(ENTITY_ID_FORMAT,
                                                 f"{DEFAULT_NAME}_{mac_id}_sensor_{parameter}",
                                                 hass=hass)
            entities.append(GnePVMonitoringSensor(entity_id, coordinator, entry, mac_id, parameter))
    async_add_entities(entities)


class GnePVMonitoringSensor(GnePVMonitoringEntity, SensorEntity):

    def __init__(self, entity_id, coordinator, config_entry, mac_id, parameter):
        super().__init__(entity_id, coordinator, config_entry, mac_id)
        self._parameter = parameter

    @property
    def name(self):
        return f"{super().name} {self._parameter}"

    @property
    def native_value(self):
        return self.get_current_data()[self._parameter]

    @property
    def native_unit_of_measurement(self):
        return PARAMETERS[self._parameter]["unit"]

    @property
    def device_class(self):
        return PARAMETERS[self._parameter]["device_class"]

    @property
    def state_class(self):
        return PARAMETERS[self._parameter]["state_class"]

    @property
    def entity_category(self):
        return PARAMETERS[self._parameter]["entity_category"]

    @property
    def icon(self):
        return PARAMETERS[self._parameter]["icon"]

    @property
    def unique_id(self):
        return f"{super().unique_id}_sensor_{self._parameter}"

    @property
    def extra_state_attributes(self):
        return {
            "raw_value": self.state
        }
