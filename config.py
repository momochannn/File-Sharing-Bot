import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1764754187:AAGCKMSMGSxOfsj6uJcvgK11rWuzjBKFzag")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "5469720"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d69086dbd5605db7bfdf334daff7b917")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001399152448"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1607338903"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001316700581"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Halo {firstname}n\nSaya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(1607338903)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
