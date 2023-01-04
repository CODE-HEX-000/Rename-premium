"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**You can get premium subscription under cheap rate.**

       **Important Message**
        First you contact Admin to check bot service active or not.
        
        **Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 20  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 60  🇮🇳/🌎 0.97$  per Month
	
	**Pay Using Upi I'd** ```aswin25@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/A_s_w_i_n_01")],         			
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/mw28xeq3")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**You can get premium subscription under cheap rate.**

        **Important Message**
        First you contact Admin to check bot service active or not.

        **Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 20  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 60  🇮🇳/🌎 0.97$  per Month
	
	**Pay Using Upi I'd** ```aswin25@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/A_s_w_i_n_01")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/mw28xeq3")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
