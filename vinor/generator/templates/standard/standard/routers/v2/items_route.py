from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from standard.dependencies import get_db


router = APIRouter()


@router.get("/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = [
        {
            "id": 1,
            "name": "Item 1",
        },
        {
            "id": 1,
            "name": "Item 1",
        },
    ]
    return items
