import json
from typing import List, Optional

from pydantic import parse_obj_as

from database.api.meta.request import make_request
from database.api.routes.material import RouteType
from database.api.schemas.material import Material


def get_all_materials(
    api_url: str = "http://localhost",
    api_port: int = 8080,
    authorization_token: Optional[str] = None,
    audience: Optional[str] = None,
    timeout: int = 3600,
    serialize_as_python_obj: bool = True,
):
    response = make_request(
        route=f"/v1/material{RouteType.all_materials}",
        request_type="GET",
        api_url=api_url,
        api_port=api_port,
        authorization_token=authorization_token,
        audience=audience,
        timeout=timeout,
    )
    if serialize_as_python_obj:
        return parse_obj_as(List[Material], json.loads(response))
    return json.loads(response)
