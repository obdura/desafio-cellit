from fastapi import FastAPI

from app.functions import get_id_from_plate, get_plate_from_id


app = FastAPI()


@app.get("/id/{plate}")
def id_from_plate(plate:str):
    """Returns the id from a plate."""
    return {'id': get_id_from_plate(plate)}


@app.get("/plate/{id}")
def plate_from_id(id:int):
    """Returns the plate from an id."""
    return {'plate': get_plate_from_id(id)}