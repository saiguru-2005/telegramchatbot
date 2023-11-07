from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN: Final='6873222085:AAG3jHjAtGto849f4m0Icacy6jOayCIzSMI'
BOT_USERNAME:Final='@saigurubot'

#commands for bot
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Thanks for chatting with me! I am Guru')

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am your bot Please type somethimg i can respond')

async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# responses bot
def handle_response(text:str)->str:
    processed:str=text.lower()
    if 'hello' in processed :
        return 'Hi'
    if 'how are you' in processed :
        return 'I am good thanks for asking hope you also good'
    if "what do you do" in processed:
        return ' I am a bot i will give responses to your questions'
    if 'tell me about your self' in processed:
        return 'I am a bot  I will answer the user questions'
    if 'fuck you' in processed:
        return 'don\'t respond to me like that pleasw'
    if 'i have a question ' in processed:
        return 'I like questions  I am here to help you'
    if "Thank you!" in processed:
        return 'You are welcome'
    if ' make me laugh' in processed:
        return 'imagine your friend face when teacher is aksing question'
    if '"How\'s your day going' in processed:
        return 'It is good I hope you also sanme'
    if ' i love you' in processed:
        return 'same i love you much'
    return ' I dont understand what you said'


async def handle_message(update: Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.chat.type
    text:str=update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type=='group':
        if BOT_USERNAME in text:
            new_text:str=text.replace(BOT_USERNAME,'').strip()
            response:str=handle_response(new_text)
        else:
            return
    else:
        response:str=handle_response(text)
    print('BOT:', response)
    await update.message.reply_text(response)

async def errors(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'update{update} caused error {context.error} ')

if __name__ == '__main__':
    print('Starting BOT.......')
    app=Application.builder().token(TOKEN).build()
       #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #error
    app.add_error_handler(errors)

    print('Polling')
    app.run_polling(poll_interval=3)







