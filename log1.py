import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger.setLevel(logging.DEBUG)
def abc():
    print('inside print statement')
    print(getattr(logging, 'DEBUG'))
    logger.warning("You are inside warning!!!")
    logger.info("You are inside info logger!!!")
    logger.debug("You are inside debug logger!")
abc()