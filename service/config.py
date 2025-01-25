import logging
from os import environ

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = environ.get("KEY")
assert SECRET_KEY != None


logging.basicConfig(
    # filename="logs.log",
    level=logging.WARNING,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",  # datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)
