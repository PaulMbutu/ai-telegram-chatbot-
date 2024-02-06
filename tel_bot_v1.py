import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

BOT_KEY = '5979065864:AAGEdnQlbf0usTqAippSR3-exGb814FclpA'

def start(update, context):
    message = "Niaje Buda Welcome to the bot!"
    keyboard = [[InlineKeyboardButton("Option 1 WATCH A MOVIE", callback_data='WATCH A MOVIE'),
                 InlineKeyboardButton("Option 2 ULIZA SWALI", callback_data='ULIZA SWALI')],
                [InlineKeyboardButton("Option 3 CHECK STOCK PRICES", callback_data='CHECK STOCK PRICES')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    option = query.data
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ati ulikua unadai opotion ya Ku" + option)

def echo(update, context):
    message_text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
    print(message_text)

def main():
    # Start the bot
    updater = Updater(BOT_KEY, use_context=True)

    # Register the command and callback handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Add a message handler to handle any message that's not a command
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

main()
