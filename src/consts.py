import json
import os

from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv("PREFIX") or "MLH!"
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

COGS = ["src.exts.hello_world"]
#   "src.exts.help",

class Colo:
    blue = 1
    red = 2
    yellow = 3

with open("meta.json") as f:
    META = json.load(f)
