import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)-15s | %(levelname)s | %(name)s | %(message)s",
)
