import json
from pathlib import Path
import sqlite3
from sqlite3 import PARSE_COLNAMES
from sqlite3 import PARSE_DECLTYPES
from typing import Dict

file_path = Path(f'{Path(__file__).parent.absolute()}\items.json')

def read_db() -> dict:
    with open(file_path, 'r') as f:
        db = json.load(f)

    return db

def write_db(item: Dict[str, str]) -> None:
    db = read_db()
    db['items'].append(item)

    with open(file_path, 'w') as f:
        json.dump(db, f)

DB_NAME = 'test.db'

def get_sql_engine():
    con = sqlite3.connect('example.db')

    return con