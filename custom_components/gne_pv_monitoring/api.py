import asyncio
import datetime
import hashlib
import json
import logging
import random
import socket
from typing import Optional

import aiohttp
import async_timeout
from aiohttp import ClientSession
from homeassistant.util import Throttle

from .const import (DATETIME_FORMAT, MIN_TIME_BETWEEN_CALLS, URL)

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)


class GnePVMonitoringApiClient:
    cache = dict()

    def __init__(
            self, app_id: str, app_secret: str, beehive_id: str
    ) -> None:
        self._app_id = app_id
        self._app_secret = app_secret
        self._beehive_id = beehive_id
        self._last_output = None

    async def async_get_data(self) -> Optional[dict]:
        output = await self._get_data_internal()
        if output is not None:
            self._last_output = output
        if self._last_output is not None:
            if "code" in self._last_output and self._last_output["code"] == 200:
                self.cache.clear()
                return self._last_output
            else:
                _LOGGER.error(
                    "Failed to retrieve data from GNE API:\n   code: %s\n   message: %s",
                    str(self._last_output["code"]),
                    self._last_output["msg"],
                )
        if len(GnePVMonitoringApiClient.cache) > 0:
            return self.cache
        return None

    @Throttle(MIN_TIME_BETWEEN_CALLS)
    async def _get_data_internal(self) -> Optional[dict]:
        return await self.api_wrapper(URL, headers=self.create_headers(), data=self.create_payload())

    async def check_errors(self) -> Optional[str]:
        output = await self._get_data_internal()
        GnePVMonitoringApiClient.cache.update(output)
        if output is not None:
            self._last_output = output
        if "code" in self._last_output and self._last_output["code"] == 200:
            return None
        return self._last_output["msg"]

    def create_headers(self) -> dict:
        rand = random.randint(1000000000, 9999999999)
        stamp = round(datetime.datetime.now().timestamp() * 1000)

        client_signature = {
            "rand": rand,
            "appId": self._app_id,
            "sign": hashlib.md5(f"{self._app_secret}{stamp}{rand}".encode()).hexdigest(),
            "stamp": stamp,
        }
        return {"client_signature": json.dumps(client_signature)}

    def create_payload(self) -> dict:
        start_time = (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime(DATETIME_FORMAT)
        end_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        return {
            "beehiveId": self._beehive_id,
            "startTransTime": start_time,
            "endTransTime": end_time,
            "queryBean": {
                "current": 1,
                "size": 100,
                "ascs": [],
                "descs": ["transTime"],
            },
        }

    async def api_wrapper(self, url: str, data: dict, headers: dict) -> dict:
        try:
            async with async_timeout.timeout(TIMEOUT):
                async with ClientSession() as session:
                    async with session.post(url, headers=headers, json=data) as response:
                        return await response.json()

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
