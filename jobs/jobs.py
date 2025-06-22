from datetime import time
from telegram.ext import Application
from dailyrepot.daylyreport import send_daily_report

def applyAsyncJobs(app: Application):
    app.job_queue.run_daily(
        send_daily_report,
        time=time(hour=18, minute=00),
        days=(0, 1, 2, 3, 4, 5, 6),
        chat_id=-1002823803500
    )