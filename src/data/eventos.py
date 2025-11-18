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

        qtd_rounds = events_utils.calculate_rounds_based_on_player_count(
            len(user_ticket_ids)
        )
        if qtd_rounds == -1:
            return False

        _generate_rounds(evento_id, qtd_rounds, user_ticket_ids, cursor)

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


def _generate_rounds(
    evento_id,
    qtd_rounds,
    user_ticket_ids,
    cursor: psycopg2.extensions.cursor,
):
    next_inserted_match_ids = []
    for i in range(1, qtd_rounds + 1):
        current_round = qtd_rounds - (i - 1)
        if i == 1:
            sql = "INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID, ROUND) VALUES (%s, %s) RETURNING ID;"
            cursor.execute(sql, (evento_id, current_round))
            next_inserted_match_ids.append(cursor.fetchone()[0])
        elif i == qtd_rounds:
            data = []
            interval = 0
            player_ticket_idx = 0
            next_match_id_idx = 0
            total_matches_this_round = int((2**i) / 2)
            for _ in range(total_matches_this_round):
                if interval - 2 == 0:
                    interval = 0
                    next_match_id_idx += 1
                interval += 1
                data.append(
                    (
                        evento_id,
                        user_ticket_ids[player_ticket_idx],
                        user_ticket_ids[player_ticket_idx + 1],
                        next_inserted_match_ids[next_match_id_idx],
                        current_round,
                    )
                )
                player_ticket_idx += 2

            sql = "INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID, PLAYER1_ID, PLAYER2_ID, NEXT_MATCH_ID, ROUND) VALUES %s;"
            execute_values(cursor, sql, data)
        else:
            data = []
            interval = 0
            next_match_id_idx = 0
            total_matches_this_round = int((2**i) / 2)
            for _ in range(total_matches_this_round):
                if interval - 2 == 0:
                    interval = 0
                    next_match_id_idx += 1
                interval += 1
                data.append(
                    (
                        evento_id,
                        next_inserted_match_ids[next_match_id_idx],
                        current_round,
                    )
                )

            sql = "INSERT INTO EVENTOS_PARTIDAS(EVENTO_ID, NEXT_MATCH_ID, ROUND) VALUES %s RETURNING ID;"
            execute_values(cursor, sql, data)
            next_inserted_match_ids = [row[0] for row in cursor.fetchall()]


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


def fetch_event_matches(evento_id):
    """
    Returns objects of (
        id,
        player1_id,
        player2_id,
        winner_id,
        next_match_id,
        round,
        round_game,
        player1_nickname,
        player2_nickname)

    grouped by round.
    """
    try:
        conn = db.create_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = """
SELECT
    EP.ID,
	EP.PLAYER1_ID,
	EP.PLAYER2_ID,
	EP.WINNER_ID,
	EP.NEXT_MATCH_ID,
	EP.ROUND,
	EP.ROUND_GAME,
	UP1.NICKNAME AS PLAYER1_NICKNAME,
	UP2.NICKNAME AS PLAYER2_NICKNAME
FROM
	EVENTOS_PARTIDAS EP
	LEFT JOIN USUARIOS UP1 ON UP1.ID = EP.PLAYER1_ID
	LEFT JOIN USUARIOS UP2 ON UP2.ID = EP.PLAYER2_ID
WHERE
	EP.EVENTO_ID = %s
ORDER BY
	ROUND, ID
"""
        cursor.execute(sql, (evento_id,))
        raw_matches_data = cursor.fetchall()

        qtd_rounds = raw_matches_data[-1][5]  # Recupera o round do último registro
        result = [[] for _ in range(qtd_rounds)]

        for match in raw_matches_data:
            result[match[5] - 1].append(
                match
            )  # Utiliza o round da partida como indice para adicionar na lista.

        return result
    finally:
        db.close_connection(conn, cursor)


def increment_match_round(match_id):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = """
UPDATE EVENTOS_PARTIDAS
SET
	ROUND_GAME = ROUND_GAME + 1
WHERE
	ID = %s
"""
        cursor.execute(sql, (match_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"[increment_match_round]: {e}")
        return False
    finally:
        db.close_connection(conn, cursor)


def set_match_winner(match_id, winner_id):
    try:
        conn = db.create_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = """
UPDATE EVENTOS_PARTIDAS
SET
	WINNER_ID = %s
WHERE
	ID = %s
RETURNING EVENTO_ID, NEXT_MATCH_ID;
"""
        cursor.execute(sql, (winner_id, match_id))
        (evento_id, next_match_id) = cursor.fetchone()
        if next_match_id:
            _set_player_next_match(winner_id, next_match_id, cursor)
        else:
            _finish_game(winner_id, evento_id, cursor)

        conn.commit()
        return True
    except Exception as e:
        print(f"[set_match_winner]: {e}")
        return False
    finally:
        db.close_connection(conn, cursor)


def _set_player_next_match(
    winner_id, next_match_id, cursor: psycopg2.extensions.cursor
):
    sql = "SELECT PLAYER1_ID, PLAYER2_ID FROM EVENTOS_PARTIDAS WHERE ID = %s"
    cursor.execute(sql, (next_match_id,))
    next_match = cursor.fetchone()
    if next_match[0]:
        sql = "UPDATE EVENTOS_PARTIDAS SET PLAYER2_ID = %s WHERE ID = %s"
    else:
        sql = "UPDATE EVENTOS_PARTIDAS SET PLAYER1_ID = %s WHERE ID = %s"
    cursor.execute(
        sql,
        (
            winner_id,
            next_match_id,
        ),
    )


def _finish_game(winner_id, evento_id, cursor: psycopg2.extensions.cursor):
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
