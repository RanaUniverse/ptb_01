
'''
This is my main file to run all things are connected mainly with this
The Database System has not implimented Yet

Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''

import sys
sys.dont_write_bytecode = True



from telegram import Update
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters

from telegram.ext import ContextTypes
from telegram.constants import ParseMode


'''
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Below will my special coding started
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
'''


import random
async def get_user_name_design(user, context: ContextTypes.DEFAULT_TYPE):
    '''Pass the user = update.message.from_user like this and it will get the name and return after makeup'''
    full_name = user.full_name
    
    designs = [
        f"1 Your Name is:\n\n<b>{full_name}</b>\n\n",
        f"2 Your Name is:\n\n<strong>{full_name}</strong>\n\n",
        f"3 Your Name is:\n\n<i>{full_name}</i>\n\n",
        f"4 Your Name is:\n\n<em>{full_name}</em>\n\n",
        f"5 Your Name is:\n\n<u>{full_name}</u>\n\n",
        f"6 Your Name is:\n\n<ins>{full_name}</ins>\n\n",
        f"7 Your Name is:\n\n<s>{full_name}</s>\n\n",
        f"8 Your Name is:\n\n<strike>{full_name}</strike>\n\n",
        f"9 Your Name is:\n\n<del>{full_name}</del>\n\n",
        f"10 Your Name is:\n\n<span class='tg-spoiler'>{full_name}</span>\n\n",
        f"11 Your Name is: \n\n<tg-spoiler>{full_name}</tg-spoiler>"
        f"12 Your Name is:\n\n<b>{full_name} <i>italic {full_name}</i></b>\n\n",
        f"13 Your Name is:\n\n<a href='http://t.me/@{user.username}/'>{full_name}</a>\n\n",
        f"14 Your Name is:\n\n<a href='tg://user?id={user.id}'>{full_name}</a>\n\n",
        f"15 Your Name is:\n\n<tg-emoji emoji-id='5368324170671202286'>{full_name}</tg-emoji>\n\n",
        f"16 Your Name is:\n\n<code>{full_name}</code>\n\n",
        f"17 Your Name is:\n\n<pre>{full_name}</pre>\n\n",
        f"18 Your Name is:\n\n<pre><code class='language-python'>{full_name}</code></pre>\n\n",
        f"19 Your Name is:\n\n<blockquote>{full_name}</blockquote>\n\n"
    ]
    
    design_str = random.choice(designs)
    
    return f"{design_str}"
    # return f"{designs}"
    # design_str = '\n'.join(designs)
    # return design_str



async def start_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (
        f"{await get_user_name_design(user, context)}\n"
        f"This is from main start_cmd function"
        f"This is for checking purpose onlu"
    )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)




async def extra_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is execute when any extra /cmd came to bot'''
    user = update.message.from_user
    user_text = update.message.text
    text = f"Hello <b>{user.full_name}</b>, You have Send me <code>{user_text}</code>\n"
    text += f"I dont understand what you want to do with this cmd pls send /help"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will send the same msg send to the bot'''
    user = update.message.from_user
    text = (f"You have send me This Text Below:\n"
            "Thanks Boss")
    await context.bot.send_message(user.id, text)






def main() -> None:
    """Start the bot."""

    application = Application.builder().token(token).build()



    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_cmd_private,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))


    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_fun))
    application.add_handler(MessageHandler(filters.Command(), extra_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()







