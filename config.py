import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "") #⚠️ Required 
    STRING_API_ID = os.environ.get("STRING_API_ID", "") # ⚠️ Required
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "") # ⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Premium_Data")     
    DB_URL  = os.environ.get("DB_URL","") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
