from pathlib import Path
import pandas as pd

from src.common.logger import logger
from src.ingestion.product_generator import ProductGenerator


def main():

    logger.info("=" * 60)
    logger.info("Generating Products Started")
    logger.info("=" * 60)

    generator = ProductGenerator()

    products = []

    TOTAL_PRODUCTS = 500

    for _ in range(TOTAL_PRODUCTS):
        products.append(generator.generate_product())

    products_df = pd.DataFrame(products)

    project_root = Path(__file__).resolve().parents[2]

    output_path = (
        project_root
        / "data"
        / "raw"
        / "products.csv"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    products_df.to_csv(
        output_path,
        index=False
    )

    logger.info(f"Generated {TOTAL_PRODUCTS} Products")
    logger.info(f"File Saved : {output_path}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()