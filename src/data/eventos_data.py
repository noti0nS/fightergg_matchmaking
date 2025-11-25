from . import db, eventos_partidas_data
from utils import eventos_utils

import psycopg2.extensions
import random


def fetch_active_events_by_user(usuario_id):
    """
    Returns a list of (
        id,
        titulo,
        descricao,
        data_inscr,
        em_andamento,
        valor_recompensa,
        qtd_players,
        qtd_subscribed_players,
        game_titulo)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
SELECT
	E.ID,
	E.TITULO,
	E.DESCRICAO,
	E.DATA_INSCR,
	E.EM_ANDAMENTO,
	E.VALOR_RECOMPENSA,
	E.QTD_PLAYERS,
	(
		SELECT
			COUNT(*)
		FROM
			EVENTOS_TICKETS ET
		WHERE
			ET.EVENTO_ID = E.ID
	) AS QTD_SUBSCRIBED_PLAYERS,
	G.TITULO
FROM
	EVENTOS E
	INNER JOIN GAMES G ON E.GAME_ID = G.ID
WHERE
	OWNER_ID = %s
	AND WINNER_ID IS NULL
ORDER BY ID
"""
        cursor.execute(sql, (usuario_id,))
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)


def fetch_deletable_events_by_user(usuario_id):
    """
    Returns a list of (
        id,
        titulo,
        data_inscr,
        valor_recompensa,
        qtd_players,
        qtd_subscribed_players,
        game_titulo)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
SELECT
	E.ID,
	E.TITULO,
	E.DATA_INSCR,
	E.VALOR_RECOMPENSA,
	E.QTD_PLAYERS,
	(
		SELECT
			COUNT(*)
		FROM
			EVENTOS_TICKETS ET
		WHERE
			ET.EVENTO_ID = E.ID
	) AS QTD_SUBSCRIBED_PLAYERS,
	G.TITULO
FROM
	EVENTOS E
	INNER JOIN GAMES G ON E.GAME_ID = G.ID
WHERE
	OWNER_ID = %s
    AND NOT EM_ANDAMENTO
ORDER BY ID
"""
        cursor.execute(sql, (usuario_id,))
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)


def fetch_available_events(logged_user_id):
    """
    Returns a list of (
        id,
        titulo,
        descricao,
        data_inscr,
        valor_recompensa,
        qtd_players,
        qtd_subscribed_players,
        game_titulo,
        owner_nickname)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
-- Cria tabela temp para usar a coluna QTD_SUBSCRIBED_PLAYERS na condicao de WHERE na select abaixo
WITH EVENTOS_WITH_QTD_SUBS_PLAYERS AS (
SELECT E.*, (
		SELECT
			COUNT(*)
		FROM
			EVENTOS_TICKETS ET
		WHERE
			ET.EVENTO_ID = E.ID
	) AS QTD_SUBSCRIBED_PLAYERS
	FROM EVENTOS E
)
SELECT
	E.ID,
	E.TITULO,
	E.DESCRICAO,
	E.DATA_INSCR,
	E.VALOR_RECOMPENSA,
	E.QTD_PLAYERS,
	E.QTD_SUBSCRIBED_PLAYERS,
	G.TITULO,
    U.NICKNAME
FROM
	EVENTOS_WITH_QTD_SUBS_PLAYERS E
	INNER JOIN GAMES G ON E.GAME_ID = G.ID
    LEFT JOIN USUARIOS U ON E.OWNER_ID = U.ID
WHERE
	NOT EM_ANDAMENTO
    AND QTD_SUBSCRIBED_PLAYERS < QTD_PLAYERS
    AND E.ID NOT IN (SELECT ET.EVENTO_ID FROM EVENTOS_TICKETS ET WHERE ET.USUARIO_ID = %s AND ET.EVENTO_ID = E.ID) -- Não incluir eventos que o usuário logado já está cadastrado
ORDER BY ID
"""
        cursor.execute(sql, (logged_user_id,))
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)


def fetch_joined_events_by_user(user_id):
    """
    Returns a list of (
        id,
        titulo,
        data_inscr,
        em_andamento,
        valor_recompensa,
        qtd_players,
        qtd_subscribed_players,
        game_titulo)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
SELECT
	E.ID,
	E.TITULO,
    E.DATA_INSCR,
	E.EM_ANDAMENTO,
	E.VALOR_RECOMPENSA,
	E.QTD_PLAYERS,
	(
		SELECT
			COUNT(*)
		FROM
			EVENTOS_TICKETS ET
		WHERE
			ET.EVENTO_ID = E.ID
	) AS QTD_SUBSCRIBED_PLAYERS,
	G.TITULO
FROM
	EVENTOS E
	INNER JOIN GAMES G ON E.GAME_ID = G.ID
WHERE
    E.ID IN (SELECT ET.EVENTO_ID FROM EVENTOS_TICKETS ET WHERE ET.USUARIO_ID = %s AND ET.EVENTO_ID = E.ID) -- Incluir apenas os eventos que o usuário logado está cadastrado
ORDER BY ID
"""
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)


def create_event_ticket(event_id, user_id) -> bool:
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO EVENTOS_TICKETS(EVENTO_ID, USUARIO_ID) VALUES (%s, %s)"
        cursor.execute(sql, (event_id, user_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"[create_event] Erro ao gravar evento: {e}")
        return False
    finally:
        db.close_connection(conn, cursor)


def create_event(new_event) -> bool:
    conn = None
    cursor = None

    try:
        conn = db.create_connection()
        if not conn:
            return False

        cursor = conn.cursor()

        query = """
INSERT INTO EVENTOS(OWNER_ID, GAME_ID, TITULO, DESCRICAO, DATA_INSCR, QTD_PLAYERS, VALOR_RECOMPENSA)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
        cursor.execute(
            query,
            (
                new_event["owner_id"],
                new_event["game_id"],
                new_event["titulo"],
                new_event["descricao"],
                new_event["data_inscr"],
                new_event["qtd_players"],
                new_event["valor_recompensa"],
            ),
        )

        conn.commit()
        return True

    except Exception as e:
        print(f"[create_event] Erro ao gravar evento: {e}")
        return False

    finally:
        db.close_connection(conn, cursor)


def update_event(updated_event) -> bool:
    conn = None
    cursor = None

    try:
        conn = db.create_connection()
        if not conn:
            print("Erro: sem conexão com o banco.")
            return False

        cursor = conn.cursor()

        query = """
            UPDATE eventos
            SET TITULO = %s,
                DESCRICAO = %s,
                VALOR_RECOMPENSA = %s
            WHERE id = %s;
        """

        cursor.execute(
            query,
            (
                updated_event["titulo"],
                updated_event["descricao"],
                updated_event["valor_recompensa"],
                updated_event["id"],
            ),
        )

        conn.commit()

        return True

    except Exception as e:
        print(f"[update_event] Erro ao atualizar evento: {e}")
        return False

    finally:
        db.close_connection(conn, cursor)


def activate_event(evento_id):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()

        sql = "SELECT USUARIO_ID FROM EVENTOS_TICKETS WHERE EVENTO_ID = %s"
        cursor.execute(sql, (evento_id,))

        user_ticket_ids = [t[0] for t in cursor.fetchall()]
        random.shuffle(user_ticket_ids)  # randomly sort first match users

        qtd_rounds = eventos_utils.calculate_rounds_based_on_player_count(
            len(user_ticket_ids)
        )
        if qtd_rounds == -1:
            return False

        eventos_partidas_data.generate_rounds(
            evento_id, qtd_rounds, user_ticket_ids, cursor
        )

        sql = "UPDATE EVENTOS SET EM_ANDAMENTO = TRUE WHERE id = %s"
        cursor.execute(sql, (evento_id,))

        conn.commit()
        return True
    except Exception as e:
        print(f"[start_event error]: {e}")
        conn.rollback()
        return False
    finally:
        db.close_connection(conn, cursor)


def fetch_event_headline(evento_id):
    """
    Returns an object of (
       titulo_evento,
       valor_recompensa,
       titulo_game,
       winner_nickname)
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
SELECT
	E.TITULO,
	E.VALOR_RECOMPENSA,
	G.TITULO,
    U.NICKNAME
FROM
	EVENTOS E
	INNER JOIN GAMES G ON E.GAME_ID = G.ID
    LEFT JOIN USUARIOS U ON U.ID = E.WINNER_ID
WHERE
	E.ID = %s
"""
        cursor.execute(sql, (evento_id,))
        return cursor.fetchone()
    finally:
        db.close_connection(conn, cursor)


def finish_event(winner_id, evento_id, cursor: psycopg2.extensions.cursor):
    sql = """
UPDATE EVENTOS
SET
	WINNER_ID = %s
WHERE
	ID = %s
RETURNING VALOR_RECOMPENSA;
"""
    cursor.execute(sql, (winner_id, evento_id))
    valor_recompensa = cursor.fetchone()[0]
    if valor_recompensa:
        sql = "UPDATE USUARIOS SET BALANCE = BALANCE + %s WHERE ID = %s"
        cursor.execute(sql, (valor_recompensa, winner_id))


def delete_event(event_id):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM EVENTOS WHERE ID = %s;"
        cursor.execute(sql, (event_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"[delete_event] Erro ao remover evento: {e}")
        return False
    finally:
        db.close_connection(conn, cursor)
