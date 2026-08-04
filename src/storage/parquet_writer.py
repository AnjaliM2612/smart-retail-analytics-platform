from pathlib import Path

from src.common.logger import logger


def write_parquet(df, layer: str, table_name: str):
    """
    Write DataFrame to the specified layer.
    """

    project_root = Path(__file__).resolve().parents[2]

    output_path = (
        project_root
        / "data"
        / layer
        / table_name
    )

    logger.info(f"Writing {layer.upper()} data to {output_path}")

    (
        df.write
        .mode("overwrite")
        .parquet(str(output_path))
    )

    logger.info(f"{layer.upper()} write completed.")