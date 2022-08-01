from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    archived = Column(Boolean, default=False)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    archived = Column(Boolean, default=False)

    source = Column(String, index=True)
    epoch_date = Column(BigInteger, index=True)
    title = Column(String, index=True)
    amount = Column(BigInteger, index=True)
    category = Column(String, index=True)
    sub_category = Column(String, index=True)
    notes = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
