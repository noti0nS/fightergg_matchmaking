import os, psycopg2


def create_connection() -> psycopg2.extensions.connection | None:
    try:
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def close_connection(
    conn: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor
):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def update_event_in_db(event: dict) -> bool:
   
    conn = None
    cursor = None

    try:
        conn = create_connection()
        if not conn:
            print("Erro: sem conexão com o banco.")
            return False

        cursor = conn.cursor()

        query = """
            UPDATE eventos
            SET nome = %s,
                data_evento = %s,
                descricao = %s
            WHERE id = %s;
        """

        cursor.execute(query, (
            event["nome"],
            event["data"],
            event["descricao"],
            event["id"]
        ))

        conn.commit()

        return True

    except Exception as e:
        print(f"[update_event_in_db] Erro ao atualizar evento: {e}")
        return False

    finally:
        close_connection(conn, cursor)

