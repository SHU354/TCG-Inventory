from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = 'cards'
    id       = Column(Integer, primary_key=True, autoincrement=True)
    name     = Column(String(100), nullable=False)
    set_name = Column(String(50),  nullable=False)
    rarity   = Column(String(20),  nullable=False)

    def __repr__(self):
        return f"<Card(id={self.id}, name='{self.name}', set='{self.set_name}', rarity='{self.rarity}')>"
