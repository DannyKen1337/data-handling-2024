
from faker import Faker
from faker_vehicle import VehicleProvider
from model_classes import Owner, Car, History  
import random

def generate_owner(n: int, male_ratio: float = 0.5,
                    locale: str = "hu_HU",
                    unique: bool = False,
                    min_age: int = 18,
                    max_age: int = 100) -> list[Owner]:
    
    assert n > 0
    assert 0 <= male_ratio <= 1
    assert min_age >= 0
    assert min_age <= max_age <= 100

    owners = []
    fake = Faker(locale)
    fake = fake if not unique else fake.unique

    for i in range(n):
        male = random.random() < male_ratio
        name = fake.name_male() if male else fake.name_female()
        phone = fake.phone_number()
        address = fake.address()
        owner_id = f"P-{str(i + 1).zfill(6)}"  
        
        owner = Owner(owner_id, name, phone, address)
        owners.append(owner)

    return owners

def generate_cars(n: int, automatic_ratio: float = 0.2,
                  locale: str = "hu_HU",
                  unique: bool = False,
                  min_year: int = 1950,
                  max_year: int = 2021) -> list[Car]:
    
    assert n > 0
    assert 1908 <= min_year
    assert min_year <= max_year <= 2021

    fake = Faker(locale)
    fake.add_provider(VehicleProvider)
    fake = fake if not unique else fake.unique

    cars = []
    for i in range(n):
        plate = fake.license_plate()
        car_type = fake.vehicle_make()  
        year = random.randint(min_year, max_year)
        
        car = Car(plate, car_type, year)
        cars.append(car)
    
    return cars


def generate_history(cars: list[Car], owners: list[Owner], n: int,
                     locale: str = "hu_HU",
                     min_mileage: int = 0,
                     max_mileage: int = 300_000) -> list[History]:
    
    assert n > 0
    assert cars and owners, "Cars and owners lists cannot be empty."
    assert min_mileage >= 0
    assert min_mileage <= max_mileage

    fake = Faker(locale)
    histories = []

    for i in range(n):
        transaction_id = f"T-{str(i + 1).zfill(6)}" 
        car = random.choice(cars)                    
        owner = random.choice(owners)                
        purchase_date = fake.date_between(start_date='-10y', end_date='today')  
        mileage = str(random.randint(min_mileage, max_mileage))  

        history = History(transaction_id, car.plate, owner.id, purchase_date, mileage)
        histories.append(history)

    return histories


owners = generate_owner(5)
cars = generate_cars(5)
histories = generate_history(cars, owners, 5)


print("Owners:")
for owner in owners:
    print(owner)

print("\nCars:")
for car in cars:
    print(car)

print("\nHistories:")
for history in histories:
    print(history)