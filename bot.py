from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application, MessageHandler, filters

from dailyrepot.daylyreport import send_daily_report
from databse.topUsersDb import initDaylyReportDb
from messagehandler.AppMessageHandler import handle_message
from utils.apikeymanager import getApiKey

def initAsyncSchedulerJobs(app: Application):
    scheduler = AsyncIOScheduler()

    daylyReportTime = "23:30" # it's 20:30 in UTC 0
    scheduler.add_job(
        send_daily_report,
        trigger="cron",
        hour=daylyReportTime.split(':')[0],
        minute=daylyReportTime.split(':')[1],
        args=[app],
    )

initDaylyReportDb()

app = Application.builder().token(getApiKey()).build()

initAsyncSchedulerJobs(app)

app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

app.run_polling()
