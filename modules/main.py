import  logging
from bing_selenium import Bing
logger = logging.getLogger(__name__)

def main() -> None:
    """Primary function to start script"""
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info('Stated')
    Bing().start()

if __name__ == "__main__":
    main()