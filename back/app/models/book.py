# On importe les types nécessaires pour définir les colonnes
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey

# On importe la classe de base qui sert de modèle commun
from .base import Base

# On crée le modèle Book qui représente la table "books" dans la base avec :
class Book(Base):

    ## ID du livre, obligatoire, avec un index pour les recherches
    id = Column ("id_book", Integer, primary_key= True, index=True)

    ## Titre du livre
    title = Column(String(255), nullable=False, index=True)

    ## Numéro ISBN du livre
    isbn = Column(String(255), nullable=False, index=True)

    ## Statut de lecture
    reading_status = Column(String(255), nullable=False, index=True)

    ## Livre en favori
    is_favorite = Column(Boolean, nullable=False)

    ## Description du livre, facultatif
    description = Column(Text, nullable=True)

    ## Lien avec une série si le livre fait partie d’une série
    id_serie = Column(Integer, ForeignKey("series.id_serie"), nullable=True)
