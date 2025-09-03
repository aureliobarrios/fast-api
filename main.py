from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {
        "hello": "world"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id
    }

# http://127.0.0.1:8000/users/100/items/abcd123?q=idk&short=True

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {
        "item_id": item_id,
        "owner_id": user_id
    }
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item