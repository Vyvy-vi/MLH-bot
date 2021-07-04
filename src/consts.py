import json
import os

from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv("PREFIX") or "MLH!"
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

COGS = [
    "src.exts.helpers",
    "src.exts.init"
]

class Colo:
    red = 1
    blue = 2
    yellow = 3

with open("meta.json") as f:
    META = json.load(f)
