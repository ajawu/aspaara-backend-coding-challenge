from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra


class PlanBase(BaseModel, extra=Extra.forbid):
    original_id: int
    talent_id: Optional[str] = None
    talent_name: Optional[str] = None
    talent_grade: Optional[str] = None
    booking_grade: Optional[str] = None
    operating_unit: str
    office_city: Optional[str] = None
    office_postal_code: str
    job_manager_name: Optional[str] = None
    job_manager_id: Optional[str] = None
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_name: Optional[str] = None
    client_id: str
    industry: Optional[str] = None
    required_skills: Optional[str] = None
    optional_skills: Optional[str] = None
    is_unassigned: Optional[bool] = False


class PlanCreate(PlanBase):
    pass


class PlanUpdate(PlanBase):
    original_id: Optional[int] = None
    operating_unit: Optional[str] = None
    office_postal_code: Optional[str] = None
    total_hours: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    client_id: Optional[str] = None


class PlanInDBBase(PlanBase):
    id: int

    class Config:
        orm_mode = True
