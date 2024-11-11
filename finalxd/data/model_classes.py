from functools import total_ordering

@total_ordering
class Owner:
    id: str
    name: str
    phone: str
    address: str

    def __init__(self, id: str, name: str, phone: str, address: str) -> None:
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        return "#{id}: {name} ({phone}, {address})".format(
            id=self.id,
            name=self.name,
            phone=self.phone,
            address=self.address
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Owner) and self.id == o.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Owner):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id.__hash__()

@total_ordering
class Car:
    plate: str
    type: str
    year: int

    def __init__(self, plate: str, type: str, year: int) -> None:
        self.plate = plate
        self.type = type
        self.year = year

    def __str__(self) -> str:
        return "{plate} ({type}, {year})".format(
            plate=self.plate,
            type=self.type,
            year=self.year,
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Car) and self.plate == o.plate

    def __hash__(self) -> int:
        return self.plate.__hash__()

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.plate < other.plate

@total_ordering
class History:
    transaction_id: str
    car_id: str
    owner_id: str
    purchase_date: str
    mileage: str

    def __init__(self, transaction_id: str, car_id: str, owner_id: str, purchase_date: str, mileage: str):
        self.transaction_id = transaction_id
        self.car_id = car_id
        self.owner_id = owner_id
        self.purchase_date = purchase_date
        self.mileage = mileage

    def __str__(self) -> str:
        return "Transaction #{transaction_id}: Car {car_id} purchased by Owner {owner_id} on {purchase_date} with {mileage} miles".format(
            transaction_id=self.transaction_id,
            car_id=self.car_id,
            owner_id=self.owner_id,
            purchase_date=self.purchase_date,
            mileage=self.mileage
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, History) and self.transaction_id == o.transaction_id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, History):
            return NotImplemented
        return self.transaction_id < other.transaction_id

    def __hash__(self) -> int:
        return self.transaction_id.__hash__()
