from . import db
from utils import events_utils
from psycopg2.extras import execute_values

import psycopg2.extensions
import random


def fetch_active_events_by_user(usuario_id):
    """
    Returns a list of (
        id,
        titulo,
        descricao,
        data_inscr_inicio,
        data_inscr_fim,
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
	E.DATA_INSCR_INICIO,
	E.DATA_INSCR_FIM,
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


def start_event(evento_id):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()

        sql = "SELECT USUARIO_ID FROM EVENTOS_TICKETS WHERE EVENTO_ID = %s"
        cursor.execute(sql, (evento_id,))

        user_ticket_ids = [t[0] for t in cursor.fetchall()]
        random.shuffle(user_ticket_ids)  # randomly sort first match users

        qtd_rounds = events_utils.calculate_rounds_based_on_player_count(
            len(user_ticket_ids)
        )
        if qtd_rounds == -1:
            return False

        _generate_brackets(evento_id, qtd_rounds, user_ticket_ids, cursor)

        sql = "UPDATE EVENTOS SET EM_ANDAMENTO = TRUE WHERE id = %s"
        cursor.execute(sql, (evento_id))

        conn.commit()
        return True
    except Exception as e:
        print(f"[start_event error]: {e}")
        conn.rollback()
        return False
    finally:
        db.close_connection(conn, cursor)


def _generate_brackets(
    evento_id,
    qtd_rounds,
    user_ticket_ids,
    cursor: psycopg2.extensions.cursor,
):
    next_inserted_match_ids = []
    for i in range(1, qtd_rounds + 1):
        is_first_match = i == qtd_rounds
        is_last_match = i == 1

        if is_last_match:
            sql = f"INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID) VALUES %s RETURNING ID;"
            cursor.execute(sql, (evento_id))
            next_inserted_match_ids.append(cursor.fetchone()[0])
        elif is_first_match:
            data = []
            interval = 0
            user_ticked_idx = 0
            next_match_id_idx = 0
            matches_on_current_round = (2**i) / 2
            for i in range(matches_on_current_round):
                if interval > 0 and interval - 2 == 0:
                    interval = 0
                    next_match_id_idx += 1
                interval += 1
                data.append(
                    (
                        evento_id,
                        user_ticket_ids[user_ticked_idx],
                        user_ticket_ids[user_ticked_idx + 1],
                        next_inserted_match_ids[next_match_id_idx],
                    )
                )
                user_ticked_idx += 2

            sql = f"INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID, PLAYER1_ID, PLAYER2_ID, NEXT_MATCH_ID) VALUES %s RETURNING ID;"
            execute_values(cursor, sql, data)

            next_inserted_match_ids = [row[0] for row in cursor.fetchall()]
        else:
            matches_on_current_round = (2**i) / 2
            data = []
            interval = 0
            next_match_id_idx = 0
            for i in range(matches_on_current_round):
                if interval > 0 and interval - 2 == 0:
                    interval = 0
                    next_match_id_idx += 1
                interval += 1
                data.append((evento_id, next_inserted_match_ids[next_match_id_idx]))

            sql = f"INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID, NEXT_MATCH_ID) VALUES %s RETURNING ID;"
            execute_values(cursor, sql, data)
            next_inserted_match_ids = [row[0] for row in cursor.fetchall()]
