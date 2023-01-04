import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5561256931:AAENFrTU2KJ-t3ZzVPJfmRq_JSeFtDIxBvM")

API_ID = int(os.environ.get("API_ID", "17529372"))

API_HASH = os.environ.get("API_HASH", "d3d1e14cf654404daee47bc48eb01c8d")

STRING = os.environ.get("STRING", "BQELehwAqPeQ4BoKidLvVVDUqaBwg8Y9dH6oGdlwbW24d9g0rXFqgM5sIgW1V6EAgy7oWwNggbL9-eUqjXadGTHtSNdRkP7XJ0Eb1CfXStnBZKlAgUKOxgWVV-VOmKSLR0sFTMt823KWqqlzkmqXepLAh1BIT-K2Sucew8EY9m0Id_Ajkzu-xadS0ZypowuMNkcljkSCdZkB3vlVa9VGLte_NmBi99WbJ_-3xhyXf26OV4m-8ovrk2Cgi_mJLCCTDevUOIN2dYNfIkRvj1MRJEuQdzFGZOeE_1O8zcVqEVeP81ob6Zuzwelv4uOdrjV00JwGyHO1Mq0jk1ERNfIybsFS34eBZwAAAABa8qsxAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
