from sqlalchemy.orm import Session

from app import crud
from app.schemas.plan import Plan, PlanCreate, PlanUpdate
from app.tests.utils import factories


def test_create_item(db: Session) -> None:
    plan = PlanCreate(**factories.PlanFactory())
    plan_obj = crud.plan.create(db=db, obj_in=plan)
    assert plan.original_id == plan_obj.original_id


def test_get_item(db: Session) -> None:
    plan_data = PlanCreate(**factories.PlanFactory())
    plan = Plan.from_orm(crud.plan.create(db=db, obj_in=plan_data))
    plan_from_db = crud.plan.get(db=db, obj_id=plan.id)
    assert plan.id == plan_from_db.id  # type: ignore


def test_update_item(db: Session) -> None:
    plan = PlanCreate(**factories.PlanFactory())
    plan_obj = crud.plan.create(db=db, obj_in=plan)
    plan_2 = PlanUpdate(**factories.PlanFactory())
    plan_obj_2 = crud.plan.update(db=db, db_obj=plan_obj, obj_in=plan_2)
    assert plan_obj.id == plan_obj_2.id
    assert plan_obj.original_id == plan_obj_2.original_id


def test_delete_item(db: Session) -> None:
    plan = PlanCreate(**factories.PlanFactory())
    plan_obj = crud.plan.create(db=db, obj_in=plan)
    crud.plan.remove(db=db, obj_id=plan_obj.id)
    plan_from_db = crud.plan.get(db=db, obj_id=plan_obj.id)
    assert plan_from_db is None
