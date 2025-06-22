from telegram import Update
from telegram.ext import ContextTypes
from dailyrepot.daylyreport import process_daily_report
from messagehandler.testcommands import showTopUsersStats

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_daily_report(update)
    if update.message == "/top":
        await showTopUsersStats(update, context)
    if update.message == "/deploy":
        await showTopUsersStats(update, context)