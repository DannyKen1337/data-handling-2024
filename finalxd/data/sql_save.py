import os
import sqlite3
from datetime import date, datetime
from model_classes import Owner, Car, History
from generator import generate_owner, generate_cars, generate_history

def write_owners(owners: list[Owner], connection: sqlite3.Connection, table_name: str = "owners"):
    script = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id TEXT PRIMARY KEY,
        name TEXT,
        phone TEXT,
        address TEXT
    );
    """
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(script)
    cursor.executemany(
        f"INSERT INTO {table_name} (id, name, phone, address) VALUES (?, ?, ?, ?)",
        [(owner.id, owner.name, owner.phone, owner.address) for owner in owners]
    )
    connection.commit()
    cursor.close()

def read_owners(connection: sqlite3.Connection, table_name: str = "owners") -> list[Owner]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    owners = [Owner(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
    cursor.close()
    return owners

def write_cars(cars: list[Car], connection: sqlite3.Connection, table_name: str = "cars"):
    script = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        plate TEXT PRIMARY KEY,
        type TEXT,
        year INTEGER
    );
    """
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(script)
    cursor.executemany(
        f"INSERT INTO {table_name} (plate, type, year) VALUES (?, ?, ?)",
        [(car.plate, car.type, car.year) for car in cars]
    )
    connection.commit()
    cursor.close()

def read_cars(connection: sqlite3.Connection, table_name: str = "cars") -> list[Car]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    cars = [Car(row[0], row[1], int(row[2])) for row in cursor.fetchall()]
    cursor.close()
    return cars

def write_histories(histories: list[History], connection: sqlite3.Connection, table_name: str = "histories"):
    script = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        transaction_id INTEGER PRIMARY KEY,
        car_id TEXT,
        owner_id TEXT,
        purchase_date TEXT,
        mileage INTEGER,
        FOREIGN KEY (car_id) REFERENCES cars (plate),
        FOREIGN KEY (owner_id) REFERENCES owners (id)
    );
    """
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(script)
    
    formatted_histories = []
    for history in histories:
        if isinstance(history.purchase_date, datetime):
            purchase_date_str = history.purchase_date.isoformat()
        else:
            print(f"Invalid purchase_date: {history.purchase_date}")
            continue
        
        formatted_histories.append(
            (history.transaction_id, history.car_id, history.owner_id, purchase_date_str, history.mileage)
        )

    # Print to check the formatted histories
    print("Formatted Histories:", formatted_histories)

    cursor.executemany(
        f"INSERT INTO {table_name} (transaction_id, car_id, owner_id, purchase_date, mileage) VALUES (?, ?, ?, ?, ?)",
        formatted_histories
    )
    connection.commit()
    cursor.close()




def read_histories(connection: sqlite3.Connection, table_name: str = "histories") -> list[History]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    histories = [History(row[0], row[1], row[2], row[3], row[4]) for row in cursor.fetchall()]
    cursor.close()
    return histories

if __name__ == "__main__":
    path = "F:/adatkez/finalxd/extract"
    db_path = os.path.join(path, "data.sqlite")
    connection = sqlite3.connect(db_path)

    # Generate sample data
    owners = generate_owner(10)
    cars = generate_cars(10)
    histories = generate_history(cars, owners, 10)

    # Write data to SQLite
    write_owners(owners, connection, table_name="owners")
    write_cars(cars, connection, table_name="cars")
    write_histories(histories, connection, table_name="histories")

    # Read data from SQLite
    read_owners_list = read_owners(connection, table_name="owners")
    read_cars_list = read_cars(connection, table_name="cars")
    read_histories_list = read_histories(connection, table_name="histories")

    connection.close()

    # Print values read from SQLite
    print("Owners:")
    for owner in read_owners_list:
        print(owner)

    print("\nCars:")
    for car in read_cars_list:
        print(car)

    print("\nHistories:")
    for history in read_histories_list:
        print(history)
