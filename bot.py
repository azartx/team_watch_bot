from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text("Test")

app = Application.builder().token("TODO:TOKEN").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
