import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27060846") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "8f39072a61dbb296f38e4ff2b6cbe478") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6875880570:AAEDi0JKiSLNuBZFTzE0P_LYHrKjfpWF44s") #⚠️ Required
    
    #premium client
    STRING = os.environ.get("STRING", "BQFE1RoAkckw_w9QDclskNdh6f6efazR21zcGWeC2ZhjQMCjjiYrwZy4xzLWYiXePq0tks1byyPlFIMoBH7zQWJWE_vjBsnwNr0gasZGL_xCwknRG0p9xX31ReHkfCPfNYafF9BXpAS2cDPPqU2TR3ICOshUtcTCQciHpfiEGWBuEPCKZQ_9wxbOJdtWfOQiDUi6Y9mc9GjdCY2LPt0apv6RhMzrGAKrysA0S2cU8NOimpa1EpU3k_myH9XjeJ4RcSPBIcFhYSdt_yT61ccwxPbvk9veQ36c3uLvGabMSp4tCTgajCI4tJiQxMtEKaK8NszLleuFOxlena9_l4I4ukmFVT39KgAAAAFpiaGKAA") #⚠️ Required 
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
