from app.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate

from .base import CRUDBase


class CRUDPlan(CRUDBase[Plan, PlanCreate, PlanUpdate]):
    # def get_filter(self) -> List[Plan]:
    #     pass
    #
    # def get_order_by(self) -> List[Plan]:
    #     pass
    pass


plan = CRUDPlan(Plan)
