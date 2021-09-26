import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.api.schemas.country import Country
from database.db import get_db
from database.schemas.country import Country as SqlCountry

router = APIRouter()

logger = logging.getLogger(__name__)


class RouteType:
    all_countries = "/all_countries"


@router.get(RouteType.all_countries, response_model=List[Country], status_code=201)
def get_all_countries(
    *, db: Session = Depends(get_db),
):
    return db.query(SqlCountry).all()
