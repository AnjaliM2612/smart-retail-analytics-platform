import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


class OrderGenerator:

    order_counter = 1

    PAYMENT_METHODS = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash"
    ]

    ORDER_STATUS = [
        "Delivered",
        "Shipped",
        "Pending",
        "Cancelled"
    ]

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        customers_path = (
            project_root
            / "data"
            / "raw"
            / "customers.csv"
        )

        products_path = (
            project_root
            / "data"
            / "raw"
            / "products.csv"
        )

        self.customers_df = pd.read_csv(customers_path)
        self.products_df = pd.read_csv(products_path)

    # ----------------------------------------------------

    def generate_order_id(self):

        order_id = f"ORD{OrderGenerator.order_counter:06d}"

        OrderGenerator.order_counter += 1

        return order_id

    # ----------------------------------------------------

    def generate_customer(self):

        customer = self.customers_df.sample(1).iloc[0]

        return customer

    # ----------------------------------------------------

    def generate_product(self):

        product = self.products_df.sample(1).iloc[0]

        return product

    # ----------------------------------------------------

    def generate_quantity(self):

        return random.randint(1, 5)

    # ----------------------------------------------------

    def generate_discount(self):

        return random.choice([0, 5, 10, 15, 20])

    # ----------------------------------------------------

    def generate_payment_method(self):

        return random.choice(self.PAYMENT_METHODS)

    # ----------------------------------------------------

    def generate_order_status(self):

        return random.choice(self.ORDER_STATUS)

    # ----------------------------------------------------

    def generate_order_date(self):

        start_date = datetime(2024, 1, 1)

        random_days = random.randint(0, 700)

        order_date = start_date + timedelta(days=random_days)

        return order_date.strftime("%Y-%m-%d")

    # ----------------------------------------------------

    def generate_order(self):

        customer = self.generate_customer()

        product = self.generate_product()

        quantity = self.generate_quantity()

        unit_price = float(product["price"])

        discount = self.generate_discount()

        gross_amount = quantity * unit_price

        discount_amount = gross_amount * discount / 100

        total_amount = round(
            gross_amount - discount_amount,
            2
        )

        return {

            "order_id": self.generate_order_id(),

            "customer_id": customer["customer_id"],

            "product_id": product["product_id"],

            "quantity": quantity,

            "unit_price": unit_price,

            "discount": discount,

            "total_amount": total_amount,

            "payment_method": self.generate_payment_method(),

            "order_status": self.generate_order_status(),

            "order_date": self.generate_order_date()

        }


if __name__ == "__main__":

    generator = OrderGenerator()

    order = generator.generate_order()

    for key, value in order.items():

        print(f"{key:<20}: {value}")