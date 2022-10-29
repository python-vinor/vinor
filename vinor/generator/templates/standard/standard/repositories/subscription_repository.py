from standard.repositories.base_repository import BaseRepository
from standard.models.subscription import Subscription


class SubscriptionRepository(BaseRepository):

    model = Subscription
    searchable_fields = ['email', 'type']

    def find_by_email_and_type(self, email: str, type: str):
        return self.db.query(self.model).where(self.model.email == email).where(self.model.type == type).first()
