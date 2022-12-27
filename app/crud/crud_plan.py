from typing import List

from sqlalchemy.orm import Session

from app.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate

from .base import CRUDBase


class CRUDPlan(CRUDBase[Plan, PlanCreate, PlanUpdate]):
    # def get_filter(self) -> List[Plan]:
    #     pass
    #
    # def get_order_by(self) -> List[Plan]:
    #     pass
    def get_multi_with_sort(
        self, db: Session, *, skip: int = 0, limit: int = 100, order_by: List[str]
    ) -> List[Plan]:
        return (
            db.query(self.model)
            .order_by(*order_by)
            .offset(skip * limit)
            .limit(limit)
            .all()
        )


plan = CRUDPlan(Plan)
