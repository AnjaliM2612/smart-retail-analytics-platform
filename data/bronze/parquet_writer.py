from pathlib import Path
from src.common.logger import logger

def write_bronze(df, table_name: str):
    """
    Write DataFrame to Bronze layer.
    """

    project_root = Path(__file__).resolve().parents[2]

    bronze_path = (
        project_root
        / "data"
        / "bronze"
        / table_name
    )

    logger.info(
        f"Writing Bronze Data -> {bronze_path}"
    )

    (
        df.write
        .mode("overwrite")
        .parquet(str(bronze_path))
    )

    logger.info("Bronze write completed.")