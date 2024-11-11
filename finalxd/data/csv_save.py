import csv
import os
from model_classes import Owner, Car, History
from generator import generate_owner, generate_cars, generate_history

def write_owners_csv(owners: list[Owner], path: str, file_name: str = "owners.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name), "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["ID", "Name", "Phone", "Address"]) 
        for owner in owners:
            writer.writerow([owner.id, owner.name, owner.phone, owner.address])

def write_cars_csv(cars: list[Car], path: str, file_name: str = "cars.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name), "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["Plate", "Type", "Year"])
        for car in cars:
            writer.writerow([car.plate, car.type, car.year])

def write_histories_csv(histories: list[History], path: str, file_name: str = "histories.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name), "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["Transaction ID", "Car ID", "Owner ID", "Purchase Date", "Mileage"]) 
        for history in histories:
            writer.writerow([history.transaction_id, history.car_id, history.owner_id, history.purchase_date, history.mileage])


if __name__ == "__main__":
    path = "F:/adatkez/finalxd/extract" 
    

    owners = generate_owner(10)
    cars = generate_cars(10)
    histories = generate_history(cars, owners, 10)

    write_owners_csv(owners, path, file_name="owners.csv")
    write_cars_csv(cars, path, file_name="cars.csv")
    write_histories_csv(histories, path, file_name="histories.csv")

    print("Data has been written to CSV files.")
