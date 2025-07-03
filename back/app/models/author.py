# On importe les types nécessaires pour définir les colonnes
from sqlalchemy import Column, Integer, String

# On importe la classe de base qui sert de modèle commun
from .base import Base

# On crée le modèle Author qui représente la table "authors" dans la base avec :
class Author(Base):

    ## L'ID de l'auteur obligatoire, avec un index pour les recherches
    id = Column ("id_author", Integer, primary_key= True, index=True)

    ## Nom de l'auteur
    name = Column(String(255), nullable=False, index=True)