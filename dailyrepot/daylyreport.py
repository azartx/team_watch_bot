from telegram import Update
from telegram.ext import ContextTypes
from databse.topUsersDb import get_today_top_users, update_user_data
from utils.constants import TG_SHORT_GROUP_ID


async def process_daily_report(update: Update):
    if update.message.chat_id != TG_SHORT_GROUP_ID:
        return

    user = update.effective_user
    if not user:
        return

    user_id = user.id
    username = user.username or f"user_{user_id}"

    update_user_data(user_id, username)

async def send_daily_report(context: ContextTypes.DEFAULT_TYPE):
    top_users = get_today_top_users()
    report = format_report(top_users)

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=report
    )

def format_report(top_users):
    if not top_users:
        return "Сегодня еще никто не писал в чате 😢"

    report = ["🏆 ТОП активных пользователей за сегодня:"]
    for i, (username, count) in enumerate(top_users, 1):
        report.append(f"{i}. @{username}: {count} сообщений")

    return "\n".join(report)