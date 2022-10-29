from standard.repositories.base_repository import BaseRepository
from standard.models.file import File


class FileRepository(BaseRepository):

    model = File

    def find_by_name(self, name: str):
        return self.db.query(self.model).filter(self.model.name == name).first()
