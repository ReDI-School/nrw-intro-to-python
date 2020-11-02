import logging

logging.basicConfig(filename='example.log',                    level=logging.DEBUG, format='%(asctime)s %(message)s')
log = logging.getLogger('MarkLogger')
log2 = logging.getLogger('JanHendrikLogger')

log.debug("This is a debug message")
log2.debug("This is a debug message from JH")
log.info("This is an information message")
log.warning("This is a warning")
log.error("This is an error")
log.critical("This is very important")
