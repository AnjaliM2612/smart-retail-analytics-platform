from pathlib import Path

import pandas as pd

from src.common.logger import logger
from src.ingestion.order_generator import OrderGenerator


def main():

    logger.info("=" * 60)
    logger.info("Generating Orders Started")
    logger.info("=" * 60)

    generator = OrderGenerator()

    orders = []

    TOTAL_ORDERS = 100000

    for _ in range(TOTAL_ORDERS):
        orders.append(generator.generate_order())

    orders_df = pd.DataFrame(orders)

    project_root = Path(__file__).resolve().parents[2]

    output_path = (
        project_root
        / "data"
        / "raw"
        / "orders.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    orders_df.to_csv(
        output_path,
        index=False
    )

    logger.info(f"Generated {TOTAL_ORDERS} Orders")
    logger.info(f"File Saved : {output_path}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()