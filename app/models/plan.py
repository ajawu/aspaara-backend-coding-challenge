from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from app.db.base_class import Base


class Plan(Base):
    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(Integer, unique=True, nullable=False, index=True)
    talent_id = Column(String)
    talent_name = Column(String)
    talent_grade = Column(String)
    booking_grade = Column(String)
    operating_unit = Column(String, nullable=False)
    office_city = Column(String)
    office_postal_code = Column(String, nullable=False)
    job_manager_name = Column(String)
    job_manager_id = Column(String)
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    client_name = Column(String)
    client_id = Column(String, nullable=False)
    industry = Column(String)
    required_skills = Column(String)
    optional_skills = Column(String)
    is_unassigned = Column(Boolean, default=True)
