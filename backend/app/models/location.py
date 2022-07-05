from typing import Optional
from datetime import datetime

from app.models.core import IDModelMixin, CoreModel
from backend.app.models.type_danger import DangerType

class LocationBase(CoreModel):
    """
    All common characteristics of our Location resource
    """
    address: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    lat: Optional[float]
    lng: Optional[str]
    hour: datetime = datetime.now()
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class LocationCreate(LocationBase):
    device_id: Optional[str]
    hour: datetime = datetime.now()
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class LocationUpdate(LocationBase):
    device_id: Optional[str]
    hour: Optional[datetime]
    danger_type: Optional[DangerType]
    nb_of_validations: Optional[int]

class LocationInDB(IDModelMixin, LocationBase):
    device_id: str
    hour: datetime
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class LocationPublic(IDModelMixin, LocationBase):
    pass
