from typing import Optional
from datetime import datetime

from app.models.core import IDModelMixin, CoreModel
from backend.app.models.type_danger import DangerType

class HistoryRecordBase(CoreModel):
    """
    All common characteristics of our HistoryRecord resource
    """
    device_id: Optional[str]
    hour: datetime = datetime.now()
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class HistoryRecordCreate(HistoryRecordBase):
    device_id: Optional[str]
    hour: datetime = datetime.now()
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class HistoryRecordUpdate(HistoryRecordBase):
    device_id: Optional[str]
    hour: Optional[datetime]
    danger_type: Optional[DangerType]
    nb_of_validations: Optional[int]

class HistoryRecordInDB(IDModelMixin, HistoryRecordBase):
    device_id: str
    hour: datetime
    location_id: int
    danger_type: DangerType
    nb_of_validations: int

class HistoryRecordPublic(IDModelMixin, HistoryRecordBase):
    pass
