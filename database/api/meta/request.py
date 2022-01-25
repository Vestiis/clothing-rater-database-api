import base64
import json
import logging
from typing import List, Optional

import requests
from pydantic import validator

from database.api.helper.google_interface import GoogleInterface

logger = logging.getLogger(__name__)


def http_call_url(host_url: str, api_app_port: Optional[int] = None):
    if "localhost" not in host_url:
        return host_url
    # if localhost and api app runs a specific port then add it to url
    if api_app_port is not None:
        return f"{host_url}:{api_app_port}"


def make_request(
    route: str,
    api_url: str = "http://localhost",
    api_port: int = 8080,
    authorization_token: Optional[str] = None,
    timeout: int = 3600,
    data: Optional[dict] = None,
    request_type: str = "POST",
):
    if not api_url.startswith("http://localhost") and authorization_token is None:
        authorization_token = GoogleInterface().generate_id_token(audience=api_url)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {authorization_token}",
    }
    request_url = http_call_url(host_url=api_url, api_app_port=api_port) + route
    response = requests.request(
        request_type, url=request_url, headers=headers, data=data, timeout=timeout,
    )
    if response.status_code not in (200, 201):
        logger.error(f"Error at {route}" f" {api_url} : {response.content}")

    response = response.text
    if not isinstance(response, str):
        response = response.decode("utf8")
    return response
