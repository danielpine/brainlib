import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s-%(lineno)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

EVENT_QUENUE = []
CONSCIOUS_QUENUE = []


def start():
    logger.info('Start')


if __name__ == "__main__":
    start()
    pass