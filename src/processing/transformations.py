from pyspark.sql.functions import (upper,lower,trim,concat_ws,initcap,when,col,count)

#---------- bronze Transformations -----------------
def standardize_names(df):
    return df.withColumn('first_name', initcap(trim(col('first_name')))) \
        .withColumn('last_name', initcap(trim(col('last_name'))))


def standardize_email(df):
    """
    Convert email to lowercase.
    """

    return df.withColumn(
        "email",
        lower(trim(col("email")))
    )

def create_full_name(df):
    """
    Create full_name column.
    """

    return df.withColumn(
        "full_name",
        concat_ws(
            " ",
            col("first_name"),
            col("last_name")
        )
    )

def fill_null_phone(df):
    """
    Replace null phone numbers.
    """

    return df.fillna(
        {
            "phone": "UNKNOWN"
        }
    )

def remove_duplicates(df):
    """
    Remove duplicate records.
    """

    return df.dropDuplicates()

#--------------------- Silver Transformations -----------------
def create_silver(df):
    """
    Keep Valid and Invalid records separate.
    """
    return df.filter(
        col("email_status").isin(["VALID", "INVALID"])
    )

#--------------------- Gold Validations -----------------
def customers_by_state(df):
    """
    Count customers by state.
    """
    return df.groupBy("State").agg(count("*").alias("total_customers"))

def customers_by_city(df):
    return df.groupBy("city").agg(count("*").alias("total_customers"))

def gender_distribution(df):
    return df.groupBy("gender").agg(count("*").alias("total_customers"))