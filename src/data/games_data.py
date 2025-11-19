from . import db


def get_all_games():
    """
    Returns a list of (
        id,
        titulo,
        descricao)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT ID, TITULO, DESCRICAO FROM GAMES")
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)
