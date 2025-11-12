from . import db


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
        qtd_subscribed_players)
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
			ET.ID = E.ID
	) AS QTD_SUBSCRIBED_PLAYERS
FROM
	EVENTOS E
WHERE
	OWNER_ID = %s
	AND WINNER_ID IS NULL
ORDER BY Id
"""
        cursor.execute(sql, (usuario_id,))
        return cursor.fetchall()
    finally:
        db.close_connection(conn, cursor)
