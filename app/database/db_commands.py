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
    x = cur.execute(f"SELECT DISTINCT user_tg_id "
                    f"FROM users "
                    f"WHERE user_tg_id={user_tg_id}").fetchone()

    if x == None:
        cur.execute(f"INSERT INTO users(user_tg_id) "
                    f"VALUES({user_tg_id})")
        con.commit()


async def db_activ_id(name_activ):
    activ_id = cur.execute(f"SELECT id "
                           f"FROM activities "
                           f"WHERE name_activity='{name_activ}'").fetchone()
    activ_id = activ_id[0]
    return activ_id


async def db_activ_name(name_id: int):
    activ_name = cur.execute(f"SELECT name_activity "
                             f"FROM activities "
                             f"WHERE id='{name_id}'").fetchone()
    activ_name = activ_name[0]
    return activ_name


async def db_user_id(user_tg_id):
    user_id = cur.execute(f"SELECT DISTINCT id "
                          f"FROM users "
                          f"WHERE user_tg_id={user_tg_id}").fetchone()
    user_id = user_id[0]
    return user_id


async def db_start_activity(name_activ: str, user_tg_id: int):
    """
    Insert in database start time of activities and id data of user
    :param name_activ: text on button what name activity user started
    :param user_tg_id: telegram user id
    """
    str_time = int(datetime.timestamp(datetime.now()))
    activ_id = await db_activ_id(name_activ)
    user_id = await db_user_id(user_tg_id)
    cur.execute(f"INSERT INTO activ_lib(id_activity, id_user, start_time) "
                f"VALUES({activ_id}, {user_id}, {str_time})")
    con.commit()


async def db_stop_activity(user_tg_id: int):
    """
    Insert in database stop time and spend time of activity
    :param user_tg_id: telegram user id
    """
    stp_time = int(datetime.timestamp(datetime.now()))
    user_id = await db_user_id(user_tg_id)
    str_time = cur.execute(f"SELECT start_time FROM activ_lib "
                           f"WHERE id_user={user_id} "
                           f"ORDER BY start_time DESC").fetchone()
    str_time = int(str_time[0])
    spnd_time = stp_time - str_time

    cur.execute(f"UPDATE activ_lib SET stop_time={stp_time}, spend_time={spnd_time} "
                f"WHERE start_time={str_time}")
    con.commit()


async def db_get_spend_time(user_tg_id) -> list:
    """
    User statistic list
    :param user_tg_id:  user telegram id
    :return: Return list of activity, time spend by user
    """
    user_id = await db_user_id(user_tg_id)

    # Get list of activity and time spend
    lst_activ = cur.execute(f"SELECT id_activity, SUM (spend_time) "
                            f"FROM activ_lib "
                            f"WHERE id_user={user_id} "
                            f"GROUP BY id_activity").fetchall()

    return lst_activ

