from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session, model):

        # Initialise la BDD ainsi que le modèle à utiliser
        self.db = db
        self.model = model

    def get(self, item_id: int):

        # Récupère un objet par son id depuis la BDD
        return self.db.query(self.model).filter_by(id=item_id).first()

    def create(self, data: dict):

        # Crée un nouvel objet avec les données fournies
        item = self.model(**data)

        # Ajoute l'objet à la session
        self.db.add(item)

        # Valide les changements dans la BDD
        self.db.commit()

        # Retourne l'objet créé
        return item

    def update(self, item_id: int, data: dict):

        # Récupère l'objet à mettre à jour
        item = self.get(item_id)
        if not item:

            # Ne retourne rien si l'objet n'existe pas
            return None
        
        # Met à jour les attributs de l'objet avec des nouvelles valeurs
        for key, value in data.items():
            setattr(item, key, value)

        # Valide les changements dans la BDD
        self.db.commit()

        # Retourne l'objet mis à jour
        return item

    def delete(self, item_id: int):

        # Récupère l'objet à supprimer
        item = self.get(item_id)
        if not item:

            # Retourne rien si l'objet n'existe pas
            return None
        
        # Supprime l'objet de la BDD
        self.db.delete(item)

        # Valide la suppression dans la BDD
        self.db.commit()
        
        # Retourne l'objet supprimé
        return item