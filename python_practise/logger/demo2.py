import logging
# from logging import *   # with this no need to write logging everytime
import demo1

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f= logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s - %(lineno)s", datefmt="%d-%b-%y %H:%M:%S")

fh= logging.FileHandler("demo2.log", mode= "w")
fh.setFormatter(f)

logger.addHandler(fh)



demo1.greet("Nikita")
demo1.greet("Adrija")


logger.debug("This is a debug message from demo2")
logger.info("This is an info message from demo2")
logger.warning("This is a warning from demo2")
