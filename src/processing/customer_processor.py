#import libraries
from pathlib import Path
from pyspark.sql import SparkSession
from src.common.logger import logger

#create Spark Session
spark = (SparkSession.builder.appName("Customer Processing").master("local[*]").getOrCreate())

#locates CSV
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = (PROJECT_ROOT
            /"data"
            /"raw"
            /"customers.csv"
            )

#read CSV
df = spark.read.option("header", True).option("inferSchema", True).csv(str(RAW_FILE))


#check Data
df.show(5)
df.printSchema()
print(f" Total Customers : {df.count()}")

#stop Spark
spark.stop()

