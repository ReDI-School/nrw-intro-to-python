from uuid import UUID, uuid4

from fastapi import FastAPI, status, Body
from pydantic.dataclasses import dataclass
from dataclasses import field

def create_uuid_as_string():
    return str(uuid4())


@dataclass
class ListItem:
    # The following fields have defaults, so they should come after any
    # non-default field
    uid: str = field(default_factory=create_uuid_as_string, init=False)
    completed: bool = False
    


todo_list = []


app = FastAPI(
    title="Todo List API",
    version="1.0.0",
    contact={
        "name": "ReDi School NRW",
        "url": "https://de.redi-school.org/nrw",
    },
    description="Simple Todo List Backend"
)


@app.get(
    '/',
    response_model=list[ListItem]
)
def show_todolist() -> list[ListItem]:
    return todo_list


def add_task(item: ListItem) -> str:
    todo_list.append(item)
    return item.uid


def delete_task(uid: str):
    # The following line is necessary to be able to work with the
    # todo_list variable. Please do not remove it!
    global todo_list
    # Filter todo_list to delete the specified task.
    

def mark_task_complete(uid: str) -> ListItem:
    # The following line is necessary to be able to work with the
    # todo_list variable. Please do not remove it!
    global todo_list
    # Iterate through the todo_list, find the element with the given
    # uid, update its completed status and return it.
