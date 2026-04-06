from data.database import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS content(id TEXT PRIMARY KEY, title TEXT, popularity INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS skills(id TEXT PRIMARY KEY, name TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS user_skills(user_id TEXT, skill_id TEXT, proficiency INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS content_skills(content_id TEXT, skill_id TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS interactions(user_id TEXT, content_id TEXT, rating INTEGER)")

    conn.commit()
    conn.close()
    