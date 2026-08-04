#libraries
from pathlib import Path
from pyspark.sql.functions import col,count

#local imports
from src.common.logger import logger
from src.common.spark_session import get_spark_session
from src.storage.parquet_writer import write_parquet
from src.processing.transformations import customers_by_city,gender_distribution,customers_by_state


# main
def main():

    logger.info("=" * 60)
    logger.info("Gold Processing Started")
    logger.info("=" * 60)

    # Create Spark Session
    spark = get_spark_session("Gold Processing")

    # Project Root
    project_root = Path(__file__).resolve().parents[2]

    # Gold Path
    silver_path = (
        project_root
        / "data"
        / "silver"
        / "customers"
    )

    logger.info(f"Reading Silver Layer : {silver_path}")

    # Read Bronze Data
    silver_df = spark.read.parquet(str(silver_path))

    logger.info(f"Silver Records : {silver_df.count()}")

    # ------------- business rules --------------------
    gold_df = customers_by_state(silver_df)

    # -------------- Gold Layer -------------------

    logger.info("Writing Gold Table Customers by State...")
    gold_df.show(5)
    write_parquet(
        gold_df,
        layer="gold",
        table_name="customers_by_state"
    )

    logger.info("Gold Layer Created Successfully.")

    # Stop Spark
    spark.stop()

    logger.info("Gold Processing Completed Successfully.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()