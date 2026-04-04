from data.database import get_connection

class UserRepository:
    def get_user(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return cur.fetchone()

class ContentRepository:
    def get_all_content(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM content")
        return [row[0] for row in cur.fetchall()]

class InteractionRepository:
    def get_user_history(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT content_id FROM interactions WHERE user_id=?", (user_id,))
        return [row[0] for row in cur.fetchall()]

    def add_interaction(self, user_id, content_id, rating):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO interactions VALUES (?, ?, 'view', ?, datetime('now'))",
                    (user_id, content_id, rating))
        conn.commit()
        conn.close()