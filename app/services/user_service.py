from sqlalchemy.orm import Session


class UserService:
    def __int__(self, db: Session):
        self.db = db

    def create_user(self):
        pass

    def get_user(self, id: int):
        pass

    def get_user_username(self, username: str):
        pass

    def update_user(
        self,
        id: int,
    ):
        pass

    def delete_user(self, id: int):
        pass
