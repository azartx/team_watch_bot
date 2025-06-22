from telegram.ext import Application, MessageHandler, filters, CommandHandler
from databse.topUsersDb import initDaylyReportDb
from jobs.jobs import applyAsyncJobs
from messagehandler.AppMessageHandler import handle_message
from utils.apikeymanager import getApiKey

initDaylyReportDb()

app = Application.builder().token(getApiKey()).build()

applyAsyncJobs(app)

app.add_handler(MessageHandler(filters.ALL, handle_message))

#app.run_polling()
