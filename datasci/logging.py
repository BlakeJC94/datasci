import logging


def setup_logging():
    log_level = logging.INFO

    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s: %(message)s',
        level=log_level,
        force=True,
    )
    return logger
