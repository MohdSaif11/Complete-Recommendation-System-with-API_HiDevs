from data.database import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # existing
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id TEXT PRIMARY KEY,
        name TEXT,
        interests TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id TEXT PRIMARY KEY,
        title TEXT,
        category TEXT,
        difficulty TEXT,
        popularity INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS interactions(
        user_id TEXT,
        content_id TEXT,
        type TEXT,
        rating INTEGER,
        created_at TEXT
    )
    """)

    # 🔥 ADD THESE (required by prompt)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS skills(
        id TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_skills(
        user_id TEXT,
        skill_id TEXT,
        proficiency INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS content_skills(
        content_id TEXT,
        skill_id TEXT
    )
    """)

    conn.commit()
    conn.close()
    