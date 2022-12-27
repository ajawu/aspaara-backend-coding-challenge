from typing import List

from sqlalchemy import or_
from sqlalchemy.orm import Query, Session

from app.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate

from .base import CRUDBase


class CRUDPlan(CRUDBase[Plan, PlanCreate, PlanUpdate]):
    def _search(self, db: Session, search_term: str) -> Query:
        return db.query(self.model).filter(
            or_(
                self.model.id == search_term,
                self.model.original_id == search_term,
                self.model.talent_id == search_term,
                self.model.talent_name == search_term,
                self.model.talent_grade == search_term,
                self.model.booking_grade == search_term,
                self.model.operating_unit == search_term,
                self.model.office_city == search_term,
                self.model.office_postal_code == search_term,
                self.model.job_manager_name == search_term,
                self.model.job_manager_id == search_term,
                self.model.client_name == search_term,
                self.model.client_id == search_term,
                self.model.industry == search_term,
            )
        )

    def get_multi_with_sort(
        self,
        db: Session,
        *,
        order_by: List[str],
        skip: int = 0,
        limit: int = 100,
        search_term: str = ""
    ) -> List[Plan]:
        if search_term:
            query = self._search(db, search_term)
        else:
            query = db.query(self.model)
        return query.order_by(*order_by).offset(skip * limit).limit(limit).all()


plan = CRUDPlan(Plan)
