import subprocess

from telegram import Update
from telegram.ext import ContextTypes

def deploy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Команда для запуска скрипта
    cmd = "/root/team_watch_bot/infra/deploy.sh"

    # Запуск процесса
    subprocess.run(
        cmd,
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
