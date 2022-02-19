from pydantic.dataclasses import dataclass
import json
from typing import Optional

from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse

from utils.database import DatabaseConnection, UnknownKeyException


@dataclass
class Animal:
    name: str
    max_age: int
    picture: str = ''

app = FastAPI(
    title="Little Zoo API",
    version="1.0.0",
    contact={
        "name": "ReDi School NRW",
        "url": "https://de.redi-school.org/nrw",
    },
    description="Example of a simple API powered by FastAPI"
)

# Create a fake database connection that stores all data in
# file on disk.
db = DatabaseConnection('zoo.json', Animal, 'name')

@app.get(
    '/list',
    response_model=list[Animal],    
)
def list_animals():
    return db.get_all_items()

@app.get(
    '/{animal_name}',
    response_model=Animal,
)
def get_single_animals(animal_name: str):
    try:
        return db.get_item_by_key(animal_name)
    except UnknownKeyException:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content='No animal by that name known',
        )

@app.delete(
    '/{animal_name}',
    status_code=status.HTTP_204_NO_CONTENT,  # expect no response from server.
)
def delete_animal(animal_name: str):
    try:
        db.delete_item_under_key(animal_name)
    except UnknownKeyException:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content='No animal by that name known',
        )

@app.post(
    "/add",
    status_code=status.HTTP_201_CREATED,  # HTTP status code for successfully creating object
)
def create_animal(animal: Animal):
    db.add_item(animal)
    return db.get_item_by_key(animal.name)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)

