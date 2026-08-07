import random
from datetime import datetime, timedelta


class ProductGenerator:

    product_counter = 1

    PRODUCTS = {
        "Electronics": [
            ("Apple iPhone 16", "Apple"),
            ("Samsung Galaxy S25", "Samsung"),
            ("Dell Inspiron 15", "Dell"),
            ("HP Pavilion", "HP"),
            ("Sony WH-1000XM5", "Sony"),
            ("LG Smart TV", "LG"),
            ("Apple Watch", "Apple"),
            ("Boat Rockerz 550", "Boat"),
            ("Lenovo ThinkPad", "Lenovo"),
            ("Samsung Tablet", "Samsung")
        ],
        "Fashion": [
            ("Nike Air Max", "Nike"),
            ("Adidas Ultraboost", "Adidas"),
            ("Puma Sneakers", "Puma"),
            ("Levi's 511 Jeans", "Levis"),
            ("Allen Solly Shirt", "Allen Solly"),
            ("Van Heusen Blazer", "Van Heusen"),
            ("US Polo T-Shirt", "US Polo"),
            ("Woodland Boots", "Woodland")
        ],
        "Home": [
            ("IKEA Study Table", "IKEA"),
            ("Nilkamal Chair", "Nilkamal"),
            ("Philips LED Lamp", "Philips"),
            ("Godrej Wardrobe", "Godrej"),
            ("Sleepwell Mattress", "Sleepwell"),
            ("Prestige Cooker", "Prestige")
        ],
        "Sports": [
            ("MRF Cricket Bat", "MRF"),
            ("Nivia Football", "Nivia"),
            ("Yonex Badminton Racket", "Yonex"),
            ("Cosco Basketball", "Cosco"),
            ("Adidas Yoga Mat", "Adidas")
        ],
        "Groceries": [
            ("Aashirvaad Atta", "Aashirvaad"),
            ("Tata Salt", "Tata"),
            ("Amul Milk", "Amul"),
            ("Fortune Rice", "Fortune"),
            ("Bru Coffee", "Bru"),
            ("Tata Tea Gold", "Tata")
        ]
    }

    SUPPLIERS = [
        "ABC Suppliers",
        "Global Retail Pvt Ltd",
        "Tech Distributors",
        "Fresh Foods Ltd",
        "Home Decor Pvt Ltd",
        "Sports Hub"
    ]

    STATUS = [
        "Active",
        "Inactive"
    ]

    def generate_product_id(self):
        product_id = f"PROD{ProductGenerator.product_counter:06d}"
        ProductGenerator.product_counter += 1
        return product_id

    def generate_category(self):
        return random.choice(list(self.PRODUCTS.keys()))

    def generate_product_details(self):
        category = self.generate_category()
        product_name, brand = random.choice(self.PRODUCTS[category])

        return {
            "category": category,
            "product_name": product_name,
            "brand": brand
        }

    def generate_price(self):
        return round(random.uniform(100, 100000), 2)

    def generate_stock_quantity(self):
        return random.randint(20, 500)

    def generate_supplier(self):
        return random.choice(self.SUPPLIERS)

    def generate_rating(self):
        return round(random.uniform(3.5, 5.0), 1)

    def generate_launch_date(self):
        start = datetime(2022, 1, 1)
        launch = start + timedelta(days=random.randint(0, 1400))
        return launch.strftime("%Y-%m-%d")

    def generate_status(self):
        return random.choice(self.STATUS)

    def generate_product(self):

        details = self.generate_product_details()

        return {
            "product_id": self.generate_product_id(),
            "product_name": details["product_name"],
            "category": details["category"],
            "brand": details["brand"],
            "price": self.generate_price(),
            "stock_quantity": self.generate_stock_quantity(),
            "supplier": self.generate_supplier(),
            "rating": self.generate_rating(),
            "launch_date": self.generate_launch_date(),
            "status": self.generate_status()
        }


if __name__ == "__main__":

    generator = ProductGenerator()

    product = generator.generate_product()

    for key, value in product.items():
        print(f"{key:<20}: {value}")