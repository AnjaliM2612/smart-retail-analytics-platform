#import libraries
import logging 
from pathlib import Path #cross platform to handle file paths

# Create logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/project.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("SmartRetail")
