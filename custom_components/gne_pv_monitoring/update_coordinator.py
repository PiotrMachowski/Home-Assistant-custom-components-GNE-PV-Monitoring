import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import GnePVMonitoringApiClient
from .const import (DOMAIN, SCAN_INTERVAL)

_LOGGER: logging.Logger = logging.getLogger(__package__)


class GnePVMonitoringDataUpdateCoordinator(DataUpdateCoordinator):

    def __init__(
            self, hass: HomeAssistant, client: GnePVMonitoringApiClient
    ) -> None:
        self.api = client
        self.raw_data = None

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self):
        try:
            self.raw_data = await self.api.async_get_data()
            return GnePVMonitoringDataUpdateCoordinator.postprocess_raw_data(self.raw_data)
        except Exception as exception:
            raise UpdateFailed() from exception

    @staticmethod
    def postprocess_raw_data(raw_data: dict) -> dict:
        processed_data = {}
        for record in raw_data["data"]["queryBean"]["records"]:
            if record["macId"] not in processed_data:
                processed_data[record["macId"]] = record
        return processed_data
