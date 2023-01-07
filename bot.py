import asyncio
from pyrogram import Client, compose,idle
import os
from aiohttp import web
from plugins.web import web_server

from info import TOKEN, API_ID, API_HASH, STRING, PORT
from plugins.cb_data import app as Client2

from aiohttp import web
from plugins.web import web_server


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))

    app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
            
else:
    
    bot.run()
