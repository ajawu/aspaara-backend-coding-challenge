from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.plan import PlanCreate
from app.tests.utils import factories


def test_create_item(client: TestClient, db: Session) -> None:
    data = factories.PlanFactory()
    data["start_date"] = data["start_date"].strftime("%d/%m/%Y %I:%M %p")
    data["end_date"] = data["end_date"].strftime("%d/%m/%Y %I:%M %p")

    response = client.post(f"{settings.API_V1_STR}/plan", json=data)
    assert response.status_code == 201
    content = response.json()
    assert "id" in content
    assert content["originalId"] == data["original_id"]


def test_read_item(client: TestClient, db: Session) -> None:
    plan_obj = crud.plan.create(db=db, obj_in=PlanCreate(**factories.PlanFactory()))
    response = client.get(f"{settings.API_V1_STR}/plan/{plan_obj.id}")
    assert response.status_code == 200
    content = response.json()
    assert plan_obj.id == content["id"]


def test_update_item(client: TestClient, db: Session) -> None:
    plan_obj = crud.plan.create(db=db, obj_in=PlanCreate(**factories.PlanFactory()))
    new_grade = "A random grade to test"
    data = {"talentGrade": new_grade}
    response = client.patch(f"{settings.API_V1_STR}/plan/{plan_obj.id}", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["talentGrade"] == new_grade


def test_delete_item(client: TestClient, db: Session) -> None:
    plan_obj = crud.plan.create(db=db, obj_in=PlanCreate(**factories.PlanFactory()))
    response = client.delete(f"{settings.API_V1_STR}/plan/{plan_obj.id}")
    assert response.status_code == 204

    response = client.delete(f"{settings.API_V1_STR}/plan/-938038")
    assert response.status_code == 404
