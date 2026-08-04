#import libraries
from pathlib import Path
from pyspark.sql import SparkSession
# from src.common.logger import logger
from src.common.spark_session import get_spark_session
from pyspark.sql.functions import concat, upper,col,concat_ws,lower, trim, when
from src.storage.parquet_writer import write_bronze
from src.processing.transformations import(
    standardize_names,
    standardize_email,create_full_name,
    fill_null_phone,remove_duplicates
)

from src.processing.validation import (
    validate_email,
    validate_phone
)

#create Spark Session
spark = get_spark_session("Customer Processing")
#locates CSV
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = (PROJECT_ROOT
            /"data"
            /"raw"
            /"customers.csv"
            )

#read CSV
customer_df = spark.read.option("header", True).option("inferSchema", True).csv(str(RAW_FILE))

#Transform Data
customer_df = standardize_names(customer_df)
customer_df = standardize_email(customer_df)
customer_df = create_full_name(customer_df)
customer_df = fill_null_phone(customer_df)
customer_df = remove_duplicates(customer_df)
#validation
customer_df = validate_email(customer_df)
customer_df = validate_phone(customer_df)

write_bronze(customer_df, "customers")

# #check Data
# customer_df.show(5)
# # df.printSchema()
# # print(f" Total Customers : {df.count()}")

# #stop Spark
# spark.stop()
customer_df.select(
    "email",
    "email_status",
    "phone",
    "phone_status"
).show(20, truncate=False)
