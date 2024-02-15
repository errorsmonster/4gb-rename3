import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "26180065")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "0a6358307acf8d0d2bf98b6827e0f5c7")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6261503766:AAHTEnsfrtbJgyWLmopUFs-5u3EnJXXdjrU")  # ⚠️ Required

    # premium 4g renaming client
    STRING = os.environ.get("STRING", "BQGPeeEAtwIYMMLrDNGOcHMKWkLQYpDwAOe9hNHgAHeg5NYWAtuDrAcwMGZqyreEKCu4KVS9qZFb9qwODdLu1GMd7mxUoYpAipgl2x5B0wFHkQwoTfkU1NFDoPVDGxf4fCw7gurw3RUqYMwHDXGTZzkzLD2F7z11qhgids8N-E1AvbawJHe99Bpob1FTFrboJGIADPo4lViD7Y3AEuJLXWzKlwDaRT6m5MSWTjUaBBj4GlIhfOz9KW2gG6NBneSQqXg-D1M3qo6Ni15nXenzkLp4izboSHcGL39Iw6Hyvf5CuTwML33Jlu_xo9gPDCUhpZ_CRwlGi7OsagAj0zVwTc2OEcOIjgAAAAFYI3yIAA")
    STRING_API_ID = os.environ.get("STRING_API_ID", "26180065")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "0a6358307acf8d0d2bf98b6827e0f5c7")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "rename")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://akmonsterprogrammer:S.Aruna1155182089@rename.etklpzs.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '5773687944').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "MrAK_LinkZz") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001923308070"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
