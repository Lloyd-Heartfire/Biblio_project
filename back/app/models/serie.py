# On importe les types nécessaires pour définir les colonnes
from sqlalchemy import Column, Integer, String, Text

# On importe la classe de base qui sert de modèle commun
from .base import Base

# On crée le modèle Serie qui représente la table "series" dans la base avec :
class Serie(Base):

    ## ID de la série, obligatoire, avec un index pour les recherches
    id = Column ("id_serie", Integer, primary_key= True, index=True)

    ## Titre de la série
    name = Column(String(255), nullable=False, index=True)

    ## Description de la série, facultatif
    description = Column(Text, nullable=True)