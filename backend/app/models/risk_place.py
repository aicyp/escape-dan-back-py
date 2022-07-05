from typing import Optional
from app.models.core import IDModelMixin, CoreModel

class RiskPlaceBase(CoreModel):
    """
    All common characteristics of our RiskPlace resource
    """
    name: Optional[str]
    location_id: Optional[int]
    number_of_records: Optional[int]

class RiskPlaceCreate(RiskPlaceBase):
    name: str
    location_id: int
    number_of_records: int

class RiskPlaceUpdate(RiskPlaceBase):
    name: Optional[str]
    location_id: Optional[int]
    number_of_records: Optional[int]

class RiskPlaceInDB(IDModelMixin, RiskPlaceBase):
    name: str
    location_id: int
    number_of_records: int

class RiskPlacePublic(IDModelMixin, RiskPlaceBase):
    pass
