import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import APP_NAME
from src.logger import get_logger


logger = get_logger(__name__)


def main():
    logger.info("%s started successfully.", APP_NAME)
    print(f"{APP_NAME} is ready.")


if __name__ == "__main__":
    main()