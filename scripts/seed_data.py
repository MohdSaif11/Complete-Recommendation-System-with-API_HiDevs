from data.database import get_connection
from data.models import create_tables

create_tables()
conn = get_connection()
cur = conn.cursor()

for i in range(1,11):
    cur.execute("INSERT OR IGNORE INTO users VALUES (?,?)",(f"u{i}",f"user{i}"))

for i in range(1,21):
    cur.execute("INSERT OR IGNORE INTO content VALUES (?, ?, ?)",(f"c{i}",f"content{i}",i))

for i in range(1,11):
    for j in range(1,5):
        cur.execute("INSERT INTO interactions VALUES (?, ?, ?)",(f"u{i}",f"c{j}",5))

conn.commit()
conn.close()
