from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from standard.repositories.setting_repository import SettingRepository
from standard.dependencies import get_db
from standard.schemas.setting_schema import SettingCreate, SettingUpdate
from standard.schemas.base_response_schema import SuccessResponse


router = APIRouter()


@router.get("")
def read_settings(
    skip: int = 0, limit: int = 10, sort: str = 'id', order='desc', search_by: str = '', search_value: str = '',
    db: Session = Depends(get_db)
):
    settings = SettingRepository(db).paginate(
        skip=skip, limit=limit,
        sort=sort, order=order,
        search_by=search_by, search_value=search_value
    )
    return SuccessResponse(
        message='Retrieve settings successfully',
        data=settings
    )


@router.get("/{id}")
def read_setting(id: int, db: Session = Depends(get_db)):
    setting = SettingRepository(db).find(id)
    if setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    return SuccessResponse(
        message='Retrieve setting successfully',
        data=setting
    )


@router.post("", status_code=status.HTTP_201_CREATED)
def create_setting(setting: SettingCreate, db: Session = Depends(get_db)):
    db_setting = SettingRepository(db).find_by_name(setting.name)
    if db_setting:
        raise HTTPException(status_code=400, detail="Name already exists")
    # db_setting = SettingRepository(db).find_by_key(setting.key)
    # if db_setting:
    #     raise HTTPException(status_code=400, detail="Key already exists")
    setting = SettingRepository(db).create(setting)
    if setting is None:
        raise HTTPException(status_code=500, detail="Failed to create Setting")
    else:
        return SuccessResponse(
            message='Created Setting',
            data=setting,
        )


@router.put("/{id}")
def update_setting(id: int, setting: SettingUpdate, db: Session = Depends(get_db)):
    db_setting = SettingRepository(db).find(id)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    setting_data = setting.dict(exclude_unset=True)
    for key, value in setting_data.items():
        setattr(db_setting, key, value)
    setting = SettingRepository(db).update(db_setting)
    return SuccessResponse(
        message='Updated Setting',
        data=setting,
    )


@router.delete("/{id}")
def delete_setting(id: int, db: Session = Depends(get_db)):
    db_setting = SettingRepository(db).find(id)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    SettingRepository(db).delete(db_setting)
    return {
        "message": "Setting was deleted successfully."
    }
