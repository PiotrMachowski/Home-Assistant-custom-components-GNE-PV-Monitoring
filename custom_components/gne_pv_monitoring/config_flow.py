from typing import Optional

import voluptuous as vol
from homeassistant import config_entries

from .api import GnePVMonitoringApiClient
from .const import (CONF_APP_ID, CONF_APP_SECRET, CONF_BEEHIVE_ID, DOMAIN)


class GnePVMonitoringFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        self._errors = {}
        self._description_placeholders = {}

    async def async_step_user(self, user_input=None):
        self._errors = {}

        if user_input is not None:
            api_client = GnePVMonitoringApiClient(
                user_input[CONF_APP_ID],
                user_input[CONF_APP_SECRET],
                user_input[CONF_BEEHIVE_ID],
            )
            error = await GnePVMonitoringFlowHandler._test_credentials(api_client)
            if error is None:
                return self.async_create_entry(
                    title=user_input[CONF_BEEHIVE_ID], data=user_input
                )
            else:
                self._errors["base"] = "auth"
                self._description_placeholders = {"error_info": error}

            return await self._show_config_form(user_input)

        user_input = {}
        user_input[CONF_APP_ID] = ""
        user_input[CONF_APP_SECRET] = ""
        user_input[CONF_BEEHIVE_ID] = ""

        return await self._show_config_form(user_input)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_APP_ID, default=user_input[CONF_APP_ID]): str,
                    vol.Required(CONF_APP_SECRET, default=user_input[CONF_APP_SECRET]): str,
                    vol.Required(CONF_BEEHIVE_ID, default=user_input[CONF_BEEHIVE_ID]): str,
                }
            ),
            errors=self._errors,
            description_placeholders=self._description_placeholders
        )

    @staticmethod
    async def _test_credentials(client: GnePVMonitoringApiClient) -> Optional[str]:
        try:
            return await client.check_errors()
        except Exception:  # pylint: disable=broad-except
            pass
        return "Unknown error"
