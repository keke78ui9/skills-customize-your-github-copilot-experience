from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items_db = [
    {"id": 1, "name": "Apple", "price": 0.99},
    {"id": 2, "name": "Banana", "price": 0.59},
]

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing["id"] == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="ID already exists")
    items_db.append(item.dict())
    return item
