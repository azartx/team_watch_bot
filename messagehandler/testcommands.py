from telegram import Update
from telegram.ext import ContextTypes

from dailyrepot.daylyreport import format_report
from databse.topUsersDb import get_today_top_users


async def showTopUsersStats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=format_report(get_today_top_users())
    )
