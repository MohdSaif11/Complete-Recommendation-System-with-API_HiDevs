from data.models import create_tables
from data.database import get_connection

create_tables()
conn = get_connection()
cur = conn.cursor()

# users
for i in range(1, 6):
    cur.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?, datetime('now'))",
                (f"u{i}", f"User{i}", "tech"))

# content
for i in range(1, 11):
    cur.execute("INSERT OR IGNORE INTO content VALUES (?, ?, ?, ?, ?)",
                (f"c{i}", f"Content{i}", "AI", "easy", i))

# 🔥 skills
cur.execute("INSERT OR IGNORE INTO skills VALUES ('s1','Python')")
cur.execute("INSERT OR IGNORE INTO skills VALUES ('s2','AI')")

# user skills
cur.execute("INSERT OR IGNORE INTO user_skills VALUES ('u1','s1',5)")

# content skills
cur.execute("INSERT OR IGNORE INTO content_skills VALUES ('c1','s1')")

conn.commit()
conn.close()
