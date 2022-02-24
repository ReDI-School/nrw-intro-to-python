"""
This module provides access to a "database".

The content of this module is not the main concern for this lecture.
Have a look for an example of

* using Object-Oriented Programming (OOP)
* using custom Exceptions
* working with Typehints
"""
from dataclasses import asdict
import json
from pathlib import Path
from typing import Type, TypeVar

class UnknownKeyException(Exception):
    pass

class TakenKeyException(Exception):
    pass


ClassToStore = TypeVar('ClassToStore')

class DatabaseConnection:
    def __init__(self, filename: str, class_to_store: Type[ClassToStore], key_column: str = 'id'):
        self._filename = filename
        # make sure the file exists
        Path(self._filename).touch()
        self._key_column = key_column
        self._class_to_store = class_to_store

    def _load_database(self) -> list[ClassToStore]:
        f = open(self._filename, 'r')
        try:
            db = json.load(f)
            # Convert dictionaries to class instances
            db = list(map(lambda d: self._class_to_store(**d), db))
        except json.decoder.JSONDecodeError:
            db = []
        f.close()
        return db
    
    def _write_database(self, db: list[ClassToStore]):
        f = open(self._filename, 'w')
        db = json.dump(list(map(asdict, db)), f)
        f.close()
        return db

    def get_all_items(self) -> list[ClassToStore]:
        return self._load_database()
    
    def get_item_by_key(self, key: object) -> ClassToStore:
        db = self._load_database()

        try:
            return next(filter(lambda e: getattr(e, self._key_column) == key, db))
        except StopIteration:
            raise UnknownKeyException(f'Key {key} already unknown')
    
    def add_item(self, obj: ClassToStore):
        db = self._load_database()
        # Check that there is no existing entry under the given ID
        if any([getattr(e, self._key_column) == key for e in db]):
            raise TakenKeyException(f'Key {key} already taken in the database.')
        db.append(obj)
        self._write_database(db)

    def delete_item_under_key(self, key: object):
        db = self._load_database()
        try:
            obj_to_delete = next(filter(lambda e: getattr(e, self._key_column) == key, db))
            db.remove(obj_to_delete)
            self._write_database(db)
        except StopIteration:
            raise UnknownKeyException(f'Key {key} already unknown')