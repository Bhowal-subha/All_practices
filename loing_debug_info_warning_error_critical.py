import logging
def test_log_level():
    log = logging.getLogger(__name__)
    handle_file = logging.FileHandler("loging.text")
    format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    handle_file.setFormatter(format)
    log.addHandler(handle_file)

    log.setLevel(logging.DEBUG)
    log.debug("Print debug info")
    log.info("Info messages")
    log.warning("Warning messages")
    log.error("error messages")
    log.critical("Critical Error")
