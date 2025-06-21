from telegram.ext import Application, MessageHandler, filters, CommandHandler
from databse.topUsersDb import initDaylyReportDb
from jobs.jobs import applyAsyncJobs
from messagehandler.AppMessageHandler import handle_message, handle_command
from utils.apikeymanager import getApiKey

initDaylyReportDb()

app = Application.builder().token(getApiKey()).build()

applyAsyncJobs(app)

app.add_handler(MessageHandler(filters.ALL, handle_message))
app.add_handler(CommandHandler(filters.ALL, handle_command))

app.run_polling()
