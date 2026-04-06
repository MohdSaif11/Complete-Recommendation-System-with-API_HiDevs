from data.database import get_connection

class ContentRepository:
    def get_all(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, popularity FROM content")
        return cur.fetchall()

class InteractionRepository:
    def get_user_history(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT content_id FROM interactions WHERE user_id=?", (user_id,))
        return [r[0] for r in cur.fetchall()]

    def add(self, user_id, content_id, rating):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO interactions VALUES (?, ?, ?)", (user_id, content_id, rating))
        conn.commit()
        conn.close()
        