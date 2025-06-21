import datetime
import sqlite3

TOP_USERS_TABLE = "top_users.db"

def initDaylyReportDb():
    conn = sqlite3.connect(TOP_USERS_TABLE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_activity
    (
        user_id
        INTEGER,
        username
        TEXT,
        message_count
        INTEGER
        DEFAULT
        0,
        date
        TEXT,
        PRIMARY
        KEY
                 (
        user_id,
        date
                 ))''')
    conn.commit()
    conn.close()

def get_today_top_users():
    today = datetime.date.today().isoformat()
    conn = sqlite3.connect(TOP_USERS_TABLE)
    c = conn.cursor()

    c.execute('''SELECT username, message_count
                 FROM user_activity
                 WHERE date = ?
                 ORDER BY message_count DESC
                     LIMIT ?''', (today))
    results = c.fetchall()
    conn.close()
    return results

def update_user_data(user_id, username):
    today = datetime.date.today().isoformat()
    conn = sqlite3.connect(TOP_USERS_TABLE)
    c = conn.cursor()

    c.execute('''SELECT message_count
                 FROM user_activity
                 WHERE user_id = ? AND date = ?''', (user_id, today))
    result = c.fetchone()

    if result:
        new_count = result[0] + 1
        c.execute('''UPDATE user_activity
                     SET message_count = ?,
                         username      = ?
                     WHERE user_id = ? AND date = ?''',
                  (new_count, username, user_id, today))
    else:
        c.execute('''INSERT INTO user_activity (user_id, username, message_count, date)
                     VALUES (?, ?, 1, ?)''', (user_id, username, today))

    conn.commit()
    conn.close()