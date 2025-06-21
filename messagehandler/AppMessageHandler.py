from telegram import Update
from telegram.ext import ContextTypes

from dailyrepot.daylyreport import process_daily_report
from messagehandler.testcommands import showTopUsersStats


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_daily_report(update)
    # other messages processing

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await showTopUsersStats(update, context)