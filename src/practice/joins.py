from pathlib import Path
from src.common.spark_session import get_spark_session
from pyspark.sql.functions import sum, desc, format_number

spark = get_spark_session('Spark Joins')

PROJECT_ROOT = Path(__file__).resolve().parents[2]

#file paths
customer_df = spark.read.option("header",True).csv(str(PROJECT_ROOT / "data" / "raw" / "customers.csv"),inferSchema=True)
product_df = spark.read.option("header",True).csv(str(PROJECT_ROOT / "data" / "raw" / "products.csv"),inferSchema=True)
order_df = spark.read.option("header",True).csv(str(PROJECT_ROOT / "data" / "raw" / "orders.csv"),inferSchema=True)

# #check the schema of the dataframes
# customer_df.printSchema()
# product_df.printSchema()
# order_df.printSchema()

# #count of records in each dataframe
# print(f"Customer Records : {customer_df.count()}")
# print(f"product Records: {product_df.count()}")
# print(f"Order Records: {order_df.count()}")

# #show the first 5 records of each dataframe
# customer_df.show(5)
# product_df.show(5)
# order_df.show(5)

customer_order_df = order_df.alias("ord").join(customer_df.alias("c"),on='customer_id',how='inner')
# customer_order_df.select("c.customer_id","c.first_name","c.last_name","ord.order_id","ord.total_amount").show(5)
# customer_order_df.show(5)

product_order_df = order_df.alias("ord").join(product_df.alias("prd"),on='product_id',how='inner')
# product_order_df.select("prd.product_id","prd.product_name","ord.order_id","ord.amount").show(5)

customer_order_product_df = product_df.alias("prd").join(customer_order_df.alias("c_ord"),on='product_id',how='inner')
# customer_order_product_df.select('c_ord.customer_id','prd.product_id','prd.product_name','c_ord.order_id','c_ord.total_amount','c_ord.quantity').show(5)

#Top Revenue Generating Products
product_revenue_df = customer_order_product_df.groupBy('product_name').agg(format_number(sum('total_amount'),2).alias('total_revenue')).orderBy('total_revenue',desc=True)
product_revenue_df.show(5)

#Revenue By Category
category_revenue_df = customer_order_product_df.groupBy('category').agg(format_number(sum('total_amount'),2).alias('Revenue_by_category')).orderBy('Revenue_by_category',desc=True)
category_revenue_df.show(5)

#Top Customers by Total Revenue
top_customers_df = customer_order_product_df.groupBy('customer_id','first_name','last_name').agg(format_number(sum('total_amount'),2).alias('total_revenue')).orderBy(desc('total_revenue'))
top_customers_df.show(5)

# Top 5 Products in Each Category