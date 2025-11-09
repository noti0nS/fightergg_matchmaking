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
        cursor.execute(
            "SELECT COUNT(*) FROM Usuarios WHERE email=%s", (email,)
        )
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
            cursor.execute(
                
        
        )