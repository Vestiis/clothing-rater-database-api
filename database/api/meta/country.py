import json
from typing import List, Optional

from pydantic import parse_obj_as

from database.api.meta.request import make_request
from database.api.routes.country import RouteType
from database.api.schemas.country import Country


def get_all_countries(
    api_url: str = "http://localhost",
    api_port: int = 8080,
    authorization_token: Optional[str] = None,
    timeout: int = 3600,
    serialize_as_python_obj: bool = True,
):
    response = make_request(
        route=f"/v1/country{RouteType.all_countries}",
        request_type="GET",
        api_url=api_url,
        api_port=api_port,
        authorization_token=authorization_token,
        timeout=timeout,
    )
    if serialize_as_python_obj:
        return parse_obj_as(List[Country], json.loads(response))
    return json.loads(response)


if __name__ == "__main__":
    print(
        get_all_countries(
            api_url="http://localhost",
            audience="https://clothing-rater-api-n7s7fuxxna-ew.a.run.app",
        )
    )
