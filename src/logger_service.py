import logging

def logger_service():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('example.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)