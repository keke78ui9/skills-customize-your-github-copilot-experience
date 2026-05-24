# FastAPI REST API Starter Code

# main.py
# 
# To run this server:
# uvicorn main:app --reload
#
# Then visit:
# http://127.0.0.1:8000 - Root endpoint
# http://127.0.0.1:8000/docs - Interactive API documentation

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the Item model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage for items (will reset when server restarts)
items: List[Item] = [
    Item(id=1, name="Example Item", description="This is a sample item"),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

# TODO: Implement the CRUD endpoints for /items below

# GET /items - List all items
# @app.get("/items")
# def get_items():
#     pass

# POST /items - Add a new item
# @app.post("/items")
# def create_item(item: Item):
#     pass

# GET /items/{id} - Get a single item by ID
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     pass

# PUT /items/{id} - Update an item
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass

# DELETE /items/{id} - Delete an item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass
