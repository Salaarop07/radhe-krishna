# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", "felling_queen_heartII")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "felling_queen_heartII")
BOT_NAME = getenv("BOT_NAME","sɪʟᴇɴᴛ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/7630ab451e85aaf175942.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5280801259").split()))
