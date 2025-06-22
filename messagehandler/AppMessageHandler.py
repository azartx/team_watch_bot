from telegram import Update
from telegram.ext import ContextTypes
from dailyrepot.daylyreport import process_daily_report
from infra.deploy import deploy
from messagehandler.testcommands import showTopUsersStats

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    await process_daily_report(update)

    if msg == "/top":
        await showTopUsersStats(update, context)
    if msg == "/deploy":
        await deploy(update, context)