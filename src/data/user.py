from . import db


def get_user_by_email(email: str) -> tuple | None:
    try:
        conn = db.create_connection()
        if conn is None:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nickname, senha FROM Usuarios WHERE email=%s", (email,)
        )
        return cursor.fetchone()
    finally:
        db.close_connection(conn, cursor)
