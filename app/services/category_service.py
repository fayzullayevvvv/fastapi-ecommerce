from sqlalchemy.orm import Session


class CategoryService:
    def __int__(self, db: Session):
        self.db = db

    def create_category(self):
        pass

    def get_category(self, id: int):
        pass

    def get_category_products(self, id: int):
        pass

    def update_category(
        self,
        id: int,
    ):
        pass

    def delete_category(self, id: int):
        pass
