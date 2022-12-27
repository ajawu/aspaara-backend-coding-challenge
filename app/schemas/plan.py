from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Extra, validator

from app.utils import camelize


class PlanBase(BaseModel):
    original_id: Optional[str] = None
    talent_id: Optional[str] = None
    talent_name: Optional[str] = None
    talent_grade: Optional[str] = None
    booking_grade: Optional[str] = None
    operating_unit: Optional[str] = None
    office_city: Optional[str] = None
    office_postal_code: Optional[str] = None
    job_manager_name: Optional[str] = None
    job_manager_id: Optional[str] = None
    total_hours: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    client_name: Optional[str] = None
    client_id: Optional[str] = None
    industry: Optional[str] = None
    required_skills: Optional[List[Dict[str, str]]] = None
    optional_skills: Optional[List[Dict[str, str]]] = None
    is_unassigned: Optional[bool] = False

    @validator("start_date", "end_date", pre=True)
    def parse_date_time(cls, v: str) -> Union[datetime, str]:
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d/%m/%Y %I:%M %p")
            except ValueError:
                return datetime.strptime(v, "%m/%d/%Y %I:%M %p")
        return v

    class Config:
        orm_mode = True
        alias_generator = camelize
        allow_population_by_field_name = True
        extra = Extra.forbid


class PlanCreate(PlanBase):
    id: Optional[int]
    original_id: str
    operating_unit: str
    office_postal_code: str
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_id: str


class PlanUpdate(PlanBase):
    pass


class Plan(PlanBase):
    id: int
