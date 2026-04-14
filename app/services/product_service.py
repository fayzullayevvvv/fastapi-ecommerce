from sqlalchemy.orm import Session


class ProductService:
    def __int__(self, db: Session):
        self.db = db

    def create_product(self):
        pass

    def get_product(self, id: int):
        pass

    def get_product_by_name(self, name: str):
        pass

    def update_product(
        self,
        id: int,
    ):
        pass

    def delete_product(self, id: int):
        pass
