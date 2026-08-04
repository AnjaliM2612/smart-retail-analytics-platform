#import libraries
from pathlib import Path

#local imports
from src.common.logger import logger
from src.common.spark_session import get_spark_session

from src.processing.transformations import (
    standardize_names,
    standardize_email,
    create_full_name,
    fill_null_phone,
    remove_duplicates,
)

from src.processing.validation import (
    validate_email,
    validate_phone,
)

from src.storage.parquet_writer import write_parquet


def main():

    logger.info("=" * 60)
    logger.info("Customer Processing Started")
    logger.info("=" * 60)

    # Create Spark Session
    spark = get_spark_session("Customer Processing")

    # Project Root
    project_root = Path(__file__).resolve().parents[2]

    # Raw Customer File
    raw_file = (
        project_root
        / "data"
        / "raw"
        / "customers.csv"
    )

    logger.info(f"Reading Raw File : {raw_file}")

    # Read Customer Data
    customer_df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(raw_file))
    )

    logger.info(f"Raw Records : {customer_df.count()}")

    #---------------- Transformations -------------

    logger.info("Applying Transformations...")

    customer_df = standardize_names(customer_df)
    customer_df = standardize_email(customer_df)
    customer_df = create_full_name(customer_df)
    customer_df = fill_null_phone(customer_df)
    customer_df = remove_duplicates(customer_df)

    logger.info("Transformations Completed.")

    # ------------- Validations --------------------

    logger.info("Applying Validations...")

    customer_df = validate_email(customer_df)
    customer_df = validate_phone(customer_df)

    logger.info("Validations Completed.")

# --------------------- bronze layer ------------------------

    logger.info("Writing Bronze Layer...")
    customer_df.show(5)
    write_parquet(
        customer_df,
        layer="bronze",
        table_name="customers"
    )

    logger.info("Bronze Layer Created Successfully.")


    #spark stop
    spark.stop()

    logger.info("Customer Processing Completed Successfully.")
    logger.info("=" * 60)



if __name__ == "__main__":
    main()