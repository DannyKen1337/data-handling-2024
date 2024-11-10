import random
from model_classes import Owner, Car, History
from generator import generate_owner, generate_cars
from xlsx_save import save_to_xlsx
from sql_save import save_to_sqlite

def generate_histories(owners, cars, num_records=10, max_mileage=300000):
    histories = []
    for i in range(num_records):
        transaction_id = f"T-{str(i+1).zfill(6)}"
        car = random.choice(cars)
        owner = random.choice(owners)
        purchase_date = f"{random.randint(2000, 2023)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        mileage = random.randint(0, max_mileage)
        histories.append(History(transaction_id, car.plate, owner.id, purchase_date, mileage))
    return histories

def main():
    # Generate sample data
    owners = generate_owner(n=10, male_ratio=0.5, locale="hu_HU", unique=True)
    cars = generate_cars(n=10, automatic_ratio=0.5, locale="hu_HU", unique=True)
    histories = generate_histories(owners, cars, num_records=10)

    # Define file paths
    xlsx_path = "output_data.xlsx"
    sqlite_path = "output_data.sqlite3"

    # Save to XLSX
    save_to_xlsx(owners, cars, histories, xlsx_path)
    print(f"Data saved to {xlsx_path}")

    # Save to SQLite
    save_to_sqlite(owners, cars, histories, sqlite_path)
    print(f"Data saved to {sqlite_path}")

if __name__ == "__main__":
    main()
