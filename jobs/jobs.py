from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application
from dailyrepot.daylyreport import send_daily_report

def applyAsyncJobs(app: Application):
    scheduler = AsyncIOScheduler()

    # daily report job
    daylyReportTime = "11:20"  # it's 20:30 in UTC 0
    scheduler.add_job(
        send_daily_report,
        trigger="cron",
        hour=daylyReportTime.split(':')[0],
        minute=daylyReportTime.split(':')[1],
        args=[app],
    )

    scheduler.start()