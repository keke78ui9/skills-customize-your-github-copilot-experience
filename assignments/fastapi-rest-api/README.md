# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test a simple RESTful API using the FastAPI framework in Python. Practice designing endpoints, handling requests, and returning JSON responses.

## � Getting Started

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and visit `http://127.0.0.1:8000` to see the welcome message
4. Visit `http://127.0.0.1:8000/docs` to explore the interactive API documentation

## �📝 Tasks

### 🛠️  Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and create a basic API endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (for running the server)
- Create a main Python file (e.g., main.py)
- Implement a root endpoint (`/`) that returns a welcome message as JSON

### 🛠️  Task 2: Create a CRUD API for Items

#### Description
Design and implement RESTful endpoints to manage a collection of items (e.g., books, products, or tasks).

#### Requirements
Completed program should:

- Define an Item model with fields like `id`, `name`, and `description`
- Implement endpoints to:
  - List all items (`GET /items`)
  - Add a new item (`POST /items`)
  - Retrieve a single item by ID (`GET /items/{id}`)
  - Update an item (`PUT /items/{id}`)
  - Delete an item (`DELETE /items/{id}`)
- Return appropriate JSON responses and status codes

#### Example
```
GET /items
[
  {"id": 1, "name": "Book", "description": "A novel"},
  {"id": 2, "name": "Pen", "description": "Blue ink"}
]

POST /items
{
  "name": "Notebook",
  "description": "Lined pages"
}
Response: {"id": 3, "name": "Notebook", "description": "Lined pages"}
```

### 🛠️  Task 3: Add Input Validation and Error Handling

#### Description
Enhance your API with proper validation and error handling to make it more robust.

#### Requirements
Completed program should:

- Add validation to ensure item names are not empty
- Return a 404 status code when an item is not found
- Handle duplicate IDs appropriately when creating items
- Return clear error messages in JSON format

#### Example
```
GET /items/999
Response (404): {"detail": "Item not found"}

POST /items
{
  "name": "",
  "description": "Invalid item"
}
Response (422): {"detail": "Item name cannot be empty"}
```
