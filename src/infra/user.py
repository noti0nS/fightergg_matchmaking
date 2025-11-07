import db


def get_user_pass(email: str) -> str | None:
    try:
        conn = db.create_connection()
        if conn is None:
            return None
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email=%s")
        password = cursor.fetchone((email,))
        if password:
            return password(0)
    finally:
        db.close_connection(conn, cursor)
    return None
