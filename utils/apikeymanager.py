from dotenv import load_dotenv
import os

def getApiKey():
    load_dotenv()
    return os.getenv("TEAM_WATCH_BOT_API_KEY")
