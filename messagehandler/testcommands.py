from telegram import Update
from telegram.ext import ContextTypes

from databse.topUsersDb import get_today_top_users

async def showTopUsersStats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(
        chat_id=context.job.chat_id,
        text=get_today_top_users()
    )