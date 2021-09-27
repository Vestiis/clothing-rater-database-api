import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.api.schemas.material import Material
from database.db import get_db
from database.schemas.material import Material as SqlMaterial

router = APIRouter()

logger = logging.getLogger(__name__)


class RouteType:
    all_materials = "/all_materials"


@router.get(RouteType.all_materials, response_model=List[Material], status_code=201)
def get_all_materials(
    *, db: Session = Depends(get_db),
):
    return db.query(SqlMaterial).all()
