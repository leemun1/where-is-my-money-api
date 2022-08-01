from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    archived: bool = False
    source: str
    epoch_date: int
    title: str
    amount: int
    category: str
    sub_category: str
    notes: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    archived: bool = False
    items: list[Item] = []

    class Config:
        orm_mode = True