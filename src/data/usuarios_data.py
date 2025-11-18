from . import db


def get_user_by_email(email: str) -> tuple | None:
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nickname, senha FROM Usuarios WHERE email=%s", (email,)
        )
        return cursor.fetchone()
    finally:
        db.close_connection(conn, cursor)


def check_email_exists(email: str) -> bool:
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE email=%s", (email,))
        result = cursor.fetchone()
        return result[0] > 0
    finally:
        db.close_connection(conn, cursor)


def check_nickname_exists(nickname: str) -> bool:
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE nickname=%s", (nickname,))
        result = cursor.fetchone()
        return result[0] > 0
    finally:
        db.close_connection(conn, cursor)


def create_user(nome_completo, nickname, email, senha):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios(nome_completo, nickname, email, senha) VALUES (%s, %s, %s, %s)",
            (nome_completo, nickname, email, senha),
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"[create_user]: {e}")
        return False
    finally:
        db.close_connection(conn, cursor)


def get_user_info(usuario_id):
    try:
        conn = db.create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute(
            "SELECT NOME_COMPLETO, EMAIL, NICKNAME, BALANCE FROM Usuarios WHERE id=%s",
            (usuario_id,),
        )
        return cursor.fetchone()
    except Exception as e:
        print(f"[get_user_info]: {e}")
    finally:
        db.close_connection(conn, cursor)
