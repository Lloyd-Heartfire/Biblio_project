from repositories.image_repository import ImageRepository
from sqlalchemy.orm import Session

class ImageController:
    def __init__(self, db: Session):
        self.repo = ImageRepository(db)

    def add_image(self, data: dict):
        return self.repo.create(data)
    
    def get_image(self, image_id: int):
        return self.repo.get(image_id)

    def get_all_images(self):
        return self.repo.get_all()

    def update_image(self, image_id: int, data: dict):
        return self.repo.update(image_id, data)

    def delete_image(self, image_id: int):
        image = self.repo.get(image_id)
        if image:
            self.repo.delete(image_id)
        return image

    def search_by_name(self, name: str):
        return self.repo.get_by_name(name)

    def search_by_url(self, url: str):
        return self.repo.get_by_url(url)