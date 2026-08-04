#libraries
from pathlib import Path
from pyspark.sql.functions import col

#local imports
from src.common.logger import logger
from src.common.spark_session import get_spark_session
from src.storage.parquet_writer import write_parquet
from src.processing.transformations import create_silver

# main
def main():

    logger.info("=" * 60)
    logger.info("Silver Processing Started")
    logger.info("=" * 60)

    # Create Spark Session
    spark = get_spark_session("Silver Processing")

    # Project Root
    project_root = Path(__file__).resolve().parents[2]

    # Bronze Path
    bronze_path = (
        project_root
        / "data"
        / "bronze"
        / "customers"
    )

    logger.info(f"Reading Bronze Layer : {bronze_path}")

    # Read Bronze Data
    bronze_df = spark.read.parquet(str(bronze_path))

    logger.info(f"Bronze Records : {bronze_df.count()}")

  # ------------- business rules --------------------

    logger.info("Applying Silver Business Rules...")

    silver_df = create_silver(bronze_df)    

    logger.info(f"Silver Records : {silver_df.count()}")

    # -------------- Silver Layer -------------------

    logger.info("Writing Silver Layer...")
    silver_df.show(5)
    write_parquet(
        silver_df,
        layer="silver",
        table_name="customers"
    )

    logger.info("Silver Layer Created Successfully.")

    # Stop Spark
    spark.stop()

    logger.info("Silver Processing Completed Successfully.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()