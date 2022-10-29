from fastapi import APIRouter, HTTPException, UploadFile, BackgroundTasks, Depends, status
from sqlalchemy.orm import Session
from standard.schemas.file_schema import FileCreate, FileResponse
from standard.schemas.base_response_schema import SuccessResponse
from standard.services.image_service import ImageService
from standard.services.storage_service import StorageService
from standard.dependencies import get_db
from standard.repositories.file_repository import FileRepository

router = APIRouter()


@router.get("/")
async def read_files(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    files = FileRepository(db).paginate(skip=skip, limit=limit)
    response_files = files.copy()
    response_files.items = []
    for file in files.items:
        response_files.items.append(
            FileResponse(
                id=file.id,
                name=file.name,
                url=await StorageService().url(file.path),
                extension=file.extension,
                mimetype=file.mimetype,
                created_at=str(file.created_at),
                updated_at=str(file.updated_at),
            )
        )
    return SuccessResponse(
        message='Retrieve file successfully',
        data=response_files
    )


@router.get("/{id}")
async def read_file(id: str, db: Session = Depends(get_db)):
    file = FileRepository(db).find(id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return SuccessResponse(
        message='Retrieve file successfully',
        data=FileResponse(
            id=file.id,
            name=file.name,
            url=await StorageService().url(file.path),
            extension=file.extension,
            mimetype=file.mimetype,
        )
    )


@router.post("/upload/", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Save original file
    file_path, file_url, file_name, file_extension, file_mimetype = await StorageService().put(file=file)

    # Save file object to database
    file = FileCreate(
        id=file_name,
        name=file_name,
        path=file_path,
        extension=file_extension,
        mimetype=file_mimetype,
    )
    file = FileRepository(db).create(file)

    # Resize image size
    if 'image' in file_mimetype:
        background_tasks.add_task(ImageService().resize_image, file_path=file_path)

    return SuccessResponse(
        message="Upload file successfully",
        data=FileResponse(
            id=file.id,
            name=file.name,
            url=file_url,
            extension=file.extension,
            mimetype=file.mimetype,
        )
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_file(id: str, db: Session = Depends(get_db)):
    file = FileRepository(db).find(id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    FileRepository(db).delete(file)
    ImageService.clean_resize_images(file_path=file.path)

    return SuccessResponse(
        message='Delete file successfully',
        data=None
    )
