from pyspark.sql.functions import (
    col,
    when,
    length
)

def validate_email(df):
    """
    Validate email format.
    """

    return df.withColumn(
        "email_status",
        when(
            col("email").rlike(
                r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
            ),
            "VALID"
        ).otherwise(
            "INVALID"
        )
    )

def validate_phone(df):
    """
    Validate Indian mobile numbers.
    """

    return df.withColumn(
        "phone_status",
        when(
            (
                length(col("phone")) == 10
            )
            &
            (
                col("phone").rlike("^[6-9][0-9]{9}$")
            ),
            "VALID"
        ).otherwise(
            "INVALID"
        )
    )