from dataclasses import dataclass, field
from functools import total_ordering

@dataclass(unsafe_hash=True)
@total_ordering
class Owner:
    id: str = field(hash=True)
    name: str = field(compare=False)
    age: int = field(compare=False)
    male: bool = field(compare=False, default=True)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Owner):
            return NotImplemented
        return self.id < o.id

@dataclass(unsafe_hash=True)
class Car:
    plate: str = field(hash=True)
    type: str = field(compare=False)
    year: int = field(compare=False)

@dataclass(unsafe_hash=True)
@total_ordering
class History:
    transaction_id: str = field(hash=True)
    car_id: str = field(compare=False)
    owner_id: str = field(compare=False)
    purchase_date: str = field(compare=False)
    mileage: int = field(compare=False)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, History):
            return NotImplemented
        return self.transaction_id < o.transaction_id

    def __eq__(self, o: object) -> bool:
        return isinstance(o, History) and self.transaction_id == o.transaction_id
