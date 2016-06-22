import logging


class LoggingForTests:
    def flog(self, log):
        logging.basicConfig(level=logging.INFO)
        flog = logging.getLogger(__name__)
        flog.info(log)
