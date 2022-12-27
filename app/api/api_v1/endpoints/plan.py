from typing import Any, List, Union

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Plan, status_code=status.HTTP_201_CREATED)
def create_plan(
    plan_details: schemas.PlanCreate, db: Session = Depends(deps.get_db)
) -> Any:
    plan = crud.plan.create(db=db, obj_in=plan_details)
    return plan


@router.get("/", response_model=List[schemas.Plan])
def get_plans(
    db: Session = Depends(deps.get_db),
    page: int = 0,
    limit: int = 100,
    order_columns: Union[List[str], None] = Query(default=None),
) -> Any:
    if order_columns:
        plan_columns = schemas.PlanUpdate().dict()
        for column in order_columns:
            if column not in plan_columns and column != "id":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Unknown column - {column}",
                )
    else:
        order_columns = ["id"]

    plans = crud.plan.get_multi_with_sort(
        db, skip=page, limit=limit, order_by=order_columns
    )
    return plans


@router.get("/{obj_id}", response_model=schemas.Plan)
def get_plan_by_id(obj_id: int, db: Session = Depends(deps.get_db)) -> Any:
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
) -> Any:
    plan = crud.plan.get(db=db, obj_id=obj_id)
    if plan:
        return crud.plan.update(db=db, db_obj=plan, obj_in=plan_details)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan with matching id not found",
        )


@router.delete("/{obj_id}")
def delete_plan(obj_id: int, db: Session = Depends(deps.get_db)) -> Any:
    plan = crud.plan.remove(db=db, obj_id=obj_id)
    if plan:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan with matching id not found",
        )
