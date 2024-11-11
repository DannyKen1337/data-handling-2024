import json
import os
from datetime import date
from typing import cast, Type
from model_classes import Owner, Car, History
from generator import generate_owner, generate_cars, generate_history

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def write_owners(owners: list[Owner], path: str, file_name: str = "owners", extension: str = ".json", pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w", encoding='utf-8') as file:
        json.dump([owner.__dict__ for owner in owners], file, indent=2 if pretty else None, ensure_ascii=False, cls=CustomJSONEncoder)

def read_owners(path: str, file_name: str = "owners", extension: str = ".json") -> list[Owner]:
    with open(os.path.join(path, file_name + extension), "r", encoding='utf-8') as file:
        return [Owner(**doc) for doc in json.load(file)]

def write_cars(cars: list[Car], path: str, file_name: str = "cars", extension: str = ".json", pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w", encoding='utf-8') as file:
        json.dump([car.__dict__ for car in cars], file, indent=2 if pretty else None, ensure_ascii=False, cls=CustomJSONEncoder)

def read_cars(path: str, file_name: str = "cars", extension: str = ".json") -> list[Car]:
    with open(os.path.join(path, file_name + extension), "r", encoding='utf-8') as file:
        return [Car(**doc) for doc in json.load(file)]

def write_histories(histories: list[History], path: str, file_name: str = "histories", extension: str = ".json", pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w", encoding='utf-8') as file:
        json.dump([history.__dict__ for history in histories], file, indent=2 if pretty else None, ensure_ascii=False, cls=CustomJSONEncoder)

def read_histories(path: str, file_name: str = "histories", extension: str = ".json") -> list[History]:
    with open(os.path.join(path, file_name + extension), "r", encoding='utf-8') as file:
        return [History(**doc) for doc in json.load(file)]

def read(entity_type: Type[object], path, file_name: str = None, extension: str = None) -> list[object]:
    if entity_type == Owner:
        return read_owners(path, file_name=file_name, extension=extension)
    elif entity_type == Car:
        return read_cars(path, file_name=file_name, extension=extension)
    elif entity_type == History:
        return read_histories(path, file_name=file_name, extension=extension)
    else:
        raise RuntimeError("Unknown type of entity")

def write(entities: list[object], path, file_name: str = None, extension: str = None, pretty=True) -> None:
    if isinstance(entities[0], Owner):
        return write_owners([cast(Owner, e) for e in entities], path, file_name=file_name, extension=extension, pretty=pretty)
    elif isinstance(entities[0], Car):
        return write_cars([cast(Car, e) for e in entities], path, file_name=file_name, extension=extension, pretty=pretty)
    elif isinstance(entities[0], History):
        return write_histories([cast(History, e) for e in entities], path, file_name=file_name, extension=extension, pretty=pretty)
    else:
        raise RuntimeError("Unknown type of entity")


if __name__ == "__main__":
    path = "F:/adatkez/finalxd/extract"


    owners = generate_owner(10)
    cars = generate_cars(10)
    histories = generate_history(cars, owners, 10)

    write_owners(owners, path, file_name="owners", extension=".json", pretty=True)
    write_cars(cars, path, file_name="cars", extension=".json", pretty=True)
    write_histories(histories, path, file_name="histories", extension=".json", pretty=True)


    read_owners_list = read_owners(path, file_name="owners", extension=".json")
    read_cars_list = read_cars(path, file_name="cars", extension=".json")
    read_histories_list = read_histories(path, file_name="histories", extension=".json")

    print(read_owners_list)
    print(read_cars_list)
    print(read_histories_list)
