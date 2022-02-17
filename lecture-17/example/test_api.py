from fastapi import FastAPI
import uvicorn
from utils.database import read_db
from utils.database import write_db, get_sql_engine
from collections import ChainMap
import emojis

app = FastAPI()

@app.get('/sqlite/create_table')
def create_table():
    # Get Database connection
    con = get_sql_engine()
    # Get Database Cursor
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE animals (
            animal_name VARCHAR,
            animal_pic VARCHAR
        );
    ''')

    return {'Info': 'Database Table created'}

@app.post('/sqlite/add_animal')
def add_user_to_sqlite(animal_name: str, animal_pic: str):
    # Get Database connection
    con = get_sql_engine()
    # Get Database Cursor
    cursor = con.cursor()


    cursor.execute(f"""
        INSERT INTO animals VALUES ('{animal_name}', '{animal_pic}')
    """)

    con.commit()
    con.close()

    return {'Info': f'Success I added {animal_name}'}

@app.get('/sqlite/get_animal')
def get_user(animal_name: str):
    # Get Database connection
    con = get_sql_engine()
    # Get Database Cursor
    cursor = con.cursor()

    animal_pics = cursor.execute(f'''
        SELECT animal_pic FROM animals WHERE animal_name = '{animal_name}'
    ''')

    for p in animal_pics:
        # Assign the pic value to animal_pic
        animal_pic = p[0]

    return {f'{animal_name} looks like': f'{emojis.encode(f":{animal_pic}:")}'}


@app.get('/')
def my_root():
    return {'Hello': 'World'}

@app.get('/goat-town')
def my_animal():
    return {'Info': 'You have to tell me which goat you want to visit'}

@app.get('/goat-town/goat')
def my_animal():
    return {'I am a': emojis.encode(':goat:')}

@app.get('/cat-town/goat')
def my_animal():
    return {'Error': 'Here is no goat'}

@app.get('/cat-town/cat')
def my_animal():
    return {'I am a': emojis.encode(':cat:')}


@app.get('/animals')
def read_animal(animal_name: str, age: int):
    animals = read_db()
    animals_dict = dict(ChainMap(*animals['items']))

    if animal_name in animals_dict.keys():
        animal_pic = emojis.encode(f':{animals_dict.get(animal_name)}:')
        return {f'{animal_name} looks like this and is {age} years old': animal_pic}
    else:
        return {'error': f'{animal_name} does not exist in database'}


@app.post("/animals")
def update_animal(animal_name: str, animal_pic: str):
    new_animal = {animal_name: animal_pic}
    
    write_db(new_animal)

    return {"info": f"Added {animal_name} to the database"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=54321)
