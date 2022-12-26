from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Plan)
def create_plan(plan_details: schemas.PlanCreate, db: Session = Depends(deps.get_db)):
    plan = crud.plan.create(db=db, obj_in=plan_details)
    return plan


@router.get("/", response_model=List[schemas.Plan])
def get_plans(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    plans = crud.plan.get_multi(db, skip=skip, limit=limit)
    return plans


@router.get("/{obj_id}", response_model=schemas.Plan)
def get_plan_by_id(obj_id: int, db: Session = Depends(deps.get_db)):
    plan = crud.plan.get(db=db, obj_id=obj_id)
    if plan:
        return plan
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan with matching id not found",
        )


@router.patch("/{obj_id}", response_model=schemas.Plan)
def update_plan(
    obj_id: int, plan_details: schemas.PlanUpdate, db: Session = Depends(deps.get_db)
):
    plan = crud.plan.get(db=db, obj_id=obj_id)
    if plan:
        return crud.plan.update(db=db, db_obj=plan, obj_in=plan_details)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan with matching id not found",
        )


@router.delete("/{obj_id}")
def delete_plan(obj_id: int, db: Session = Depends(deps.get_db)):
    plan = crud.plan.remove(db=db, obj_id=obj_id)
    if plan:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan with matching id not found",
        )
