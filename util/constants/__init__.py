import logging
import os
from dotenv.main import load_dotenv

load_dotenv

__all__ = (
  "Client"
)

log = logging.getLogger(__name__)

class Client(NamedTuple):
  name = "Vaquero bot"
  default_prefix = "!"
  guild_id = 932264473408966656
  test_guild_id = 866235308416040971
  version = "0.0.1"
  bot_version = "0.0.1"
  token = os.getenv("DISCORD_TOKEN")