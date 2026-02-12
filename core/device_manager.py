# main.py

import logging
from core.engine import Engine

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def main():
    logger = setup_logging()
    try:
        engine = Engine()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()