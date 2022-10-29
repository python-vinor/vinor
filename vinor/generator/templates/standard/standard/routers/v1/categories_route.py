from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from standard.repositories.category_repository import CategoryRepository
from standard.dependencies import get_db
from standard.schemas.category_schema import CategoryCreate, CategoryUpdate
from standard.schemas.base_response_schema import SuccessResponse


router = APIRouter()


@router.get("")
def read_categories(
    skip: int = 0, limit: int = 10, sort: str = 'id', order='desc', search_by: str = '', search_value: str = '',
    db: Session = Depends(get_db)
):
    categories = CategoryRepository(db).paginate(
        skip=skip, limit=limit,
        sort=sort, order=order,
        search_by=search_by, search_value=search_value
    )
    return SuccessResponse(
        message='Retrieve car brands successfully',
        data=categories
    )


@router.get("/{id}")
def read_category(id: int, db: Session = Depends(get_db)):
    category = CategoryRepository(db).find(id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return SuccessResponse(
        message='Retrieve car brand successfully',
        data=category
    )


@router.post("", status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = CategoryRepository(db).find_by_title(category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="Name already exists")
    category = CategoryRepository(db).create(category)
    if category is None:
        raise HTTPException(status_code=500, detail="Failed to create Category")
    else:
        return SuccessResponse(
            message='Created Category',
            data=category,
        )


@router.put("/{id}")
def update_category(id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = CategoryRepository(db).find(id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)
    category = CategoryRepository(db).update(db_category)
    return SuccessResponse(
        message='Updated Category',
        data=category,
    )


@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    db_category = CategoryRepository(db).find(id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    CategoryRepository(db).delete(db_category)
    return {
        "message": "Category was deleted successfully."
    }
