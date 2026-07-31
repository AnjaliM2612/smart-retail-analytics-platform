import csv
from pathlib import Path

from src.common.logger import logger
from src.ingestion.customer_generator import CustomerGenerator

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = RAW_DATA_PATH / "customers.csv"

def generate_customers(number_of_customers: int):
    logger.info(f"Generating {number_of_customers} customers ...")
    generator = CustomerGenerator()

    headers = [
        "customer_id",
        "first_name",
        "last_name",
        "gender",
        "email",
        "phone",
        "date_of_birth",
        "city",
        "state",
        "country",
        "pincode"
    ]

    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=headers
        )

        writer.writeheader()

        for customer_number in range(
            1,
            number_of_customers + 1
        ):

            customer = generator.generate_customer(
                customer_number
            )

            writer.writerow(customer)

            if customer_number % 1000 == 0:

                logger.info(
                    f"{customer_number} customers generated..."
                )

    logger.info("Customer generation completed successfully.")

    print(f"\nCSV saved at:\n{OUTPUT_FILE}")

if __name__ == "__main__":

    NUMBER_OF_CUSTOMERS = 10000

    generate_customers(
        NUMBER_OF_CUSTOMERS
    )