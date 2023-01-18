from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (DOMAIN, NAME)


class GnePVMonitoringEntity(CoordinatorEntity):
    def __init__(self, entity_id, coordinator, config_entry, mac_id):
        super().__init__(coordinator)
        self.entity_id = entity_id
        self.config_entry = config_entry
        self.mac_id = mac_id

    @property
    def name(self):
        return f"{NAME} {self.mac_id}"

    @property
    def unique_id(self):
        return f"{self.config_entry.entry_id}_{self.mac_id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.mac_id)},
            "name": f"{NAME} {self.mac_id}",
        }

    def get_current_data(self) -> dict:
        return self.coordinator.data[self.mac_id]
