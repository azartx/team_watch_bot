from telegram import Update
from telegram.ext import ContextTypes
from dailyrepot.daylyreport import process_daily_report

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_daily_report(update)
    # other messages processing