import sqlite3 as sq3

# Connection to DB
# con = sq3.connect('trivia_box_library.db')
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
                "id_activity INTEGER UNIQUE NOT NULL,"
                "id_user INTEGER UNIQUE NOT NULL,"
                "start_time INTEGER,"
                "stop_time INTEGER,"
                "spend_time INTEGER)")

    con.commit()
