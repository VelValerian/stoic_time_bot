import sqlite3 as sq3
from datetime import datetime

# Connection to DB
con = sq3.connect('stoic_traker_bot.db')
# Create connection for work with DB
cur = con.cursor()


async def db_start():
    """
    Create Table if NOT exists in DB
    """
    # Create user TABLE
    cur.execute("CREATE TABLE IF NOT EXISTS users ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "user_tg_id INTEGER UNIQUE NOT NULL,"
                "admin_status INTEGER DEFAULT 0)")

    # Create Activity TABLE
    cur.execute("CREATE TABLE IF NOT EXISTS activities ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name_activity TEXT UNIQUE NOT NULL)")

    # Create user activity TABLE
    cur.execute("CREATE TABLE IF NOT EXISTS activ_lib ("
                "id_activity INTEGER NOT NULL,"
                "id_user INTEGER NOT NULL,"
                "start_time INTEGER,"
                "stop_time INTEGER,"
                "spend_time INTEGER)")

    con.commit()


async def db_add_new_user(user_tg_id: int):
    """
    Insert telegram user id if it not exists into the database
    :param user_tg_id: telegram user id
    """
    x = cur.execute(f"SELECT DISTINCT user_tg_id FROM users WHERE user_tg_id={user_tg_id}").fetchone()

    if x == None:
        cur.execute(f"INSERT INTO users(user_tg_id) VALUES({user_tg_id})")
        con.commit()


async def db_start_activity(name_activ: str, user_tg_id: int):
    """
    Insert in database start time of activities and id data of user
    :param name_activ: text on button what name activity user started
    :param user_tg_id: telegram user id
    """
    str_time = int(datetime.timestamp(datetime.now()))
    activ_id = cur.execute(f"SELECT id FROM activities WHERE name_activity='{name_activ}'").fetchone()
    activ_id = activ_id[0]
    user_id = cur.execute(f"SELECT DISTINCT id FROM users WHERE user_tg_id={user_tg_id}").fetchone()
    user_id = user_id[0]

    cur.execute(f"INSERT INTO activ_lib(id_activity, id_user, start_time) VALUES({activ_id}, {user_id}, {str_time})")
    con.commit()


async def db_stop_activity(user_tg_id: int):
    """
    Insert in database stop time and spend time of activity
    :param user_tg_id: telegram user id
    """
    stp_time = int(datetime.timestamp(datetime.now()))
    user_id = cur.execute(f"SELECT DISTINCT id FROM users WHERE user_tg_id={user_tg_id}").fetchone()
    user_id = user_id[0]
    str_time = cur.execute(f"SELECT start_time FROM activ_lib WHERE id_user={user_id} "
                           f"ORDER BY start_time DESC").fetchone()
    str_time = int(str_time[0])
    spnd_time = stp_time - str_time

    cur.execute(f"UPDATE activ_lib SET stop_time={stp_time}, spend_time={spnd_time} WHERE start_time={str_time}")
    con.commit()
