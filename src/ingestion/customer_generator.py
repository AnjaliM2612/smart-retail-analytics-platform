import random
import string

from faker import Faker
from src.common.logger import logger

fake = Faker("en_IN")


class CustomerGenerator:

    def __init__(self):
        self.used_emails = set()

        self.email_domains = [
            "gmail.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com"
        ]

    def generate_customer_id(self, customer_number: int) -> str:
        """
        Generate a unique customer ID.
        """

        customer_id = f"CUST{customer_number:06d}"

        logger.info(f"Generated Customer ID: {customer_id}")

        return customer_id

    def generate_name(self) -> tuple[str, str]:
        """
        Generate first and last name.
        """

        first_name = fake.first_name()
        last_name = fake.last_name()

        logger.info(f"Generated Name: {first_name} {last_name}")

        return first_name, last_name

    def generate_email(self, first_name: str, last_name: str) -> str:
        """
        Generate a unique email address.
        """

        while True:

            suffix = "".join(
                random.choices(
                    string.ascii_lowercase + string.digits,
                    k=4
                )
            )

            domain = random.choice(self.email_domains)

            email = (
                f"{first_name.lower()}."
                f"{last_name.lower()}."
                f"{suffix}@{domain}"
            )

            if email not in self.used_emails:
                self.used_emails.add(email)

                logger.info(f"Generated Email: {email}")

                return email

    def generate_phone(self) -> str:
        """
        Generate an Indian mobile number.
        """

        first_digit = random.choice(["6", "7", "8", "9"])

        remaining_digits = "".join(
            random.choices(
                string.digits,
                k=9
            )
        )

        phone = first_digit + remaining_digits

        logger.info(f"Generated Phone Number: {phone}")

        return phone

    def generate_gender(self) -> str:
        """
        Generate gender.
        """

        gender = random.choice(
            [
                "Male",
                "Female"
            ]
        )

        logger.info(f"Generated Gender: {gender}")

        return gender

    def generate_dob(self) -> str:
        """
        Generate date of birth.
        """

        dob = fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        )

        logger.info(f"Generated DOB: {dob}")

        return str(dob)

    def generate_address(self) -> dict:
        """
        Generate customer address.
        """

        address = {
            "city": fake.city(),
            "state": fake.state(),
            "country": "India",
            "pincode": fake.postcode()
        }

        logger.info(f"Generated Address: {address}")

        return address

    def generate_customer(self, customer_number: int) -> dict:
        """
        Generate a complete customer record.
        """

        customer_id = self.generate_customer_id(customer_number)

        first_name, last_name = self.generate_name()

        email = self.generate_email(
            first_name,
            last_name
        )

        phone = self.generate_phone()

        gender = self.generate_gender()

        dob = self.generate_dob()

        address = self.generate_address()

        customer = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "email": email,
            "phone": phone,
            "date_of_birth": dob,
            "city": address["city"],
            "state": address["state"],
            "country": address["country"],
            "pincode": address["pincode"]
        }

        logger.info(f"Generated Customer Record Successfully")

        return customer


if __name__ == "__main__":

    generator = CustomerGenerator()

    customer = generator.generate_customer(1)

    print(customer)