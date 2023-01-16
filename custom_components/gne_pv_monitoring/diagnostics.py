from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .update_coordinator import GnePVMonitoringDataUpdateCoordinator


async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]:
    if hass.data.get(DOMAIN) is None or entry.entry_id not in hass.data[DOMAIN]:
        return {}

    coordinator: GnePVMonitoringDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    await coordinator.async_refresh()
    return coordinator.raw_data
