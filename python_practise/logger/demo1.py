import logging

## root logger
# logging.basicConfig(filename="demo1.log", filemode ="a", level=logging.ERROR, format= "%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
## logging.disable()
##default filemode is append

# logger.debug("This is a debug message.")
# logging.info("This is a info message.")
# logging.warning("This is a warning message.")
# logging.error("This is a error message.")
# logging.critical("This is a critical message.")
#

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f= logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s - %(lineno)s", datefmt="%d-%b-%Y %H:%M:%S")

fh= logging.FileHandler("demo1.log",mode= "w")
fh.setFormatter(f)

logger.addHandler(fh)


# Function that does something and logs
def greet(name):
    logger.info(f"Greeting {name}")
    print(f"Hello, {name}!")

def nameCheck(name):
    if len(name) < 2:
        logger.debug("Checking for name length..")
        return "Invalid name!"
    elif name.isspace():
        logger.debug("Checking if name is a space...")
        return "Invalid name!"
    elif name.isalpha():
        logger.debug("Checking if name is an alphabet..")
        return "name is valid"
    elif name.replace(" ","").isalpha():
        logger.debug("Checking for full name...")
        return "name is valid"
    else:
        logger.debug("Failed all checks")
        return "Invalid name!"


print(nameCheck('Alxender123'))
