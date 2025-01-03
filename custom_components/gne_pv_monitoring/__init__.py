import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .api import GnePVMonitoringApiClient
from .const import (CONF_APP_ID, CONF_APP_SECRET, CONF_BEEHIVE_ID, DOMAIN, PLATFORMS)
from .update_coordinator import GnePVMonitoringDataUpdateCoordinator

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})

    app_id = entry.data.get(CONF_APP_ID)
    app_secret = entry.data.get(CONF_APP_SECRET)
    beehive_id = entry.data.get(CONF_BEEHIVE_ID)

    client = GnePVMonitoringApiClient(app_id, app_secret, beehive_id)

    coordinator = GnePVMonitoringDataUpdateCoordinator(hass, client=client)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
