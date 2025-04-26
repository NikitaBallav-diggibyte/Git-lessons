from logging import *

logger = getLogger(__name__)
logger.setLevel(20)

f = Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")

fh = FileHandler("exception.log", mode ="a")
fh.setFormatter(f)

logger.addHandler(fh)

class AccessDenied(Exception):
    pass

try:
    ag = int(input("Enter your age: "))
    if ag < 18:
        raise AccessDenied("Access denied")
    logger.info(f"A user having {ag} has logged in.")

except Exception as e:
    logger.exception("Exception occured")