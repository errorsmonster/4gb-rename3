import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27060846") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "8f39072a61dbb296f38e4ff2b6cbe478") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6875880570:AAEDi0JKiSLNuBZFTzE0P_LYHrKjfpWF44s") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "BQFE1RoAJgJXA0KR1PWAMQzkIj-9pGHiyCw60y6UL7nl83p_QOcfv737Afo_XWE75nUugRcQA4YbmyufnZptPIJ_iIFGyGdXWfGvQZuZDgCgqD8N0OU55OEix_Rb8HdvteCRZRUr2HgRhSfmsy7ZxQ9vKtTbDx1LAOxJfuG6e8f1YuVfh1ExGDK0HFr-gQ9gENhH6HZiMnTS_eZ7s0gX5rpS7I0-lOmAwtyF8ZsJ2XdDV1amYjJROfZxP5EyvC5VRCSEJQAvjD0nyFC4wgH1Q_Sud611TBdwWs_42n73Pdg8m5Q22E-8O7bjZYwnge0iyNH_1xdS9biuGAPNl4TTV0ao58FfTQAAAAFpiaGKAA") #⚠️ Required 
    STRING_API_ID = os.environ.get('STRING_API_ID', '21288218')
    STRING_API_HASH = os.environ.get('STRING_API_HASH', 'dd47d5c4fbc31534aa764ef9918b3acd')
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Premium_Data")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://PREMIUMRENAME:PREMIUMRENAME@cluster0.vaqtymk.mongodb.net/?retryWrites=true&w=majority") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6065594762').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Kdramaland") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001971176803")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
