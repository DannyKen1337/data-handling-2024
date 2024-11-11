import os
import pandas as pd
from model_classes import Owner, Car, History
from generator import generate_owner, generate_cars, generate_history

def write_owners_xlsx(owners: list[Owner], writer: pd.ExcelWriter) -> None:
    owners_df = pd.DataFrame([owner.__dict__ for owner in owners])
    owners_df.to_excel(writer, sheet_name='Owners', index=False)

def write_cars_xlsx(cars: list[Car], writer: pd.ExcelWriter) -> None:
    cars_df = pd.DataFrame([car.__dict__ for car in cars])
    cars_df.to_excel(writer, sheet_name='Cars', index=False)

def write_histories_xlsx(histories: list[History], writer: pd.ExcelWriter) -> None:
    histories_df = pd.DataFrame([history.__dict__ for history in histories])
    histories_df.to_excel(writer, sheet_name='Histories', index=False)

def write_to_xlsx(owners: list[Owner], cars: list[Car], histories: list[History], path: str, file_name: str = "data.xlsx") -> None:
    with pd.ExcelWriter(os.path.join(path, file_name)) as writer:
        write_owners_xlsx(owners, writer)
        write_cars_xlsx(cars, writer)
        write_histories_xlsx(histories, writer)


if __name__ == "__main__":
    path = "F:/adatkez/finalxd/extract"  

    owners = generate_owner(10)
    cars = generate_cars(10)
    histories = generate_history(cars, owners, 10)

    write_to_xlsx(owners, cars, histories, path, file_name="data.xlsx")

    print("Data has been written to XLSX file.")
