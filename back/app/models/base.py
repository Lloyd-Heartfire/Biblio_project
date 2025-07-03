# On importe les outils pour créer des colonnes avec des types (entier, date)
from sqlalchemy import Column, DateTime

# On importe ce qu’il faut pour créer une classe de base réutilisable
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# On importe la date et l’heure actuelles
from datetime import datetime

# On importe un outil pour modifier du texte
import re

# Cette classe sera la base de toutes les autres tables
@as_declarative()
class Base:

    # Chaque table aura une date de création automatique
    created_at = Column(DateTime, default=datetime.utcnow)

    # Cette fonction donne un nom à la table en fonction du nom de la classe
    @declared_attr
    def __tablename__(cls) -> str:
        # Exemple : si la classe s’appelle "BookCount", la table s’appellera "book_count"
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()