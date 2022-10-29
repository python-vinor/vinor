from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from standard.repositories.subscription_repository import SubscriptionRepository
from standard.dependencies import get_db
from standard.schemas.subscription_schema import SubscriptionCreate, SubscriptionUpdate
from standard.schemas.base_response_schema import SuccessResponse


router = APIRouter()


@router.get("/")
def read_subscriptions(
    skip: int = 0, limit: int = 10, sort: str = 'id', order='desc', search_by: str = '', search_value: str = '',
    db: Session = Depends(get_db)
):
    subscriptions = SubscriptionRepository(db).paginate(
        skip=skip, limit=limit,
        sort=sort, order=order,
        search_by=search_by, search_value=search_value
    )
    return SuccessResponse(
        message='Retrieve subscriptions successfully',
        data=subscriptions
    )


@router.get("/{id}")
def read_subscription(id: int, db: Session = Depends(get_db)):
    subscription = SubscriptionRepository(db).find(id)
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return SuccessResponse(
        message='Retrieve car brand successfully',
        data=subscription
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = SubscriptionRepository(db).find_by_email_and_type(email=subscription.email, type=subscription.type)
    if db_subscription is None:
        db_subscription = SubscriptionRepository(db).create(subscription)
    return SuccessResponse(
        message='Created Subscription',
        data=db_subscription,
    )


@router.put("/{id}")
def update_subscription(id: int, subscription: SubscriptionUpdate, db: Session = Depends(get_db)):
    db_subscription = SubscriptionRepository(db).find(id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription_data = subscription.dict(exclude_unset=True)
    for key, value in subscription_data.items():
        setattr(db_subscription, key, value)
    subscription = SubscriptionRepository(db).update(db_subscription)
    return SuccessResponse(
        message='Updated Subscription',
        data=subscription,
    )


@router.delete("/{id}")
def delete_subscription(id: int, db: Session = Depends(get_db)):
    db_subscription = SubscriptionRepository(db).find(id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    SubscriptionRepository(db).delete(db_subscription)
    return {
        "message": "Subscription was deleted successfully."
    }
