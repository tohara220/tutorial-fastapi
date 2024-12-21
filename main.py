from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def process_item(items: List[str]):
    for item in items:
        print(item)


def process_item_dict(prices: Dict[str, float]):
    """key: str, value: float"""
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)