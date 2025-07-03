# On importe les types nécessaires pour définir les colonnes
from sqlalchemy import Column, Integer, String, Text

# On importe la classe de base qui sert de modèle commun
from .base import Base

# On crée le modèle Image qui représente la table "images" dans la base avec :
class Image(Base):

    ## ID de l'image, obligatoire, avec un index pour les recherches
    id = Column ("id_image", Integer, primary_key= True, index=True)

    ## URL de l'image
    url = Column(Text, nullable=False)

    ## Nom de l'image, facultatif
    name = Column(String(255), nullable=True, index=True)