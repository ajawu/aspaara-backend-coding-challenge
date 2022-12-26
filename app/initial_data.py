import logging

import ijson

from app.db.session import SessionLocal
from app.models import Plan
from app.schemas import PlanCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    plans = []
    for plan in ijson.items(open("planning.json"), "item"):
        plans.append(PlanCreate(**plan).dict())
        if len(plans) == 3000:
            db.bulk_insert_mappings(Plan, plans)
            plans = []
    db.bulk_insert_mappings(Plan, plans)
    db.commit()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
