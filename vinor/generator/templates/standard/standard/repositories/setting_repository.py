from standard.repositories.base_repository import BaseRepository
from standard.models.setting import Setting


class SettingRepository(BaseRepository):

    model = Setting

    def find_by_name(self, name: str):
        return self.db.query(self.model).filter(self.model.name == name).first()

    def find_by_key(self, key: str):
        return self.db.query(self.model).filter(self.model.key == key).first()
