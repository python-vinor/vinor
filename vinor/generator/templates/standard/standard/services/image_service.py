from os import path, remove
from PIL import Image


DEFAULT_RESIZE_SIZES = [
    {
        "width": 1280,
        "height": 720
    },
    {
        "width": 640,
        "height": 480
    }
]


class ImageService:

    @staticmethod
    async def resize_image(file_path: str):
        basename = path.basename(file_path)
        file_name, file_extension = path.splitext(basename)
        for size in DEFAULT_RESIZE_SIZES:
            size_defined = size['height'], size['width']
            file_path_sized = f"{path.dirname(file_path)}/{file_name}_{str(size['height'])}{file_extension}"
            image = Image.open(file_path, mode="r")
            image.thumbnail(size_defined)
            image.save(file_path_sized)
            print(f"[SUCCESS] Resize images: {file_path_sized}")

    @staticmethod
    def clean_resize_images(file_path: str):
        # Delete original image
        if path.exists(file_path):
            remove(file_path)

        # Delete resized image
        basename = path.basename(file_path)
        file_name, file_extension = path.splitext(basename)
        for size in DEFAULT_RESIZE_SIZES:
            file_path_sized = f"{path.dirname(file_path)}/{file_name}_{str(size['height'])}{file_extension}"
            if path.exists(file_path_sized):
                remove(file_path_sized)
            print(f"[SUCCESS] Deleted resize images: {file_path_sized}")
