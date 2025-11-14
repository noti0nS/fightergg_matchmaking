import math

QTD_PLAYERS_LIMITS = [4, 8, 16, 32, 64]


def calculate_rounds_based_on_player_count(qtd_players):
    """
    Retorna a quantidade de rounds com base na quantidade de jogadores.

    A relação é log2(n): o número de rounds necessários para um torneio
    eliminatório simples com n jogadores (n = 2^x) é x.

    Parâmetros
    ----------
    qtd_players : int
        Quantidade de jogadores (deve estar em QTD_PLAYERS_LIMITS).

    Retorno
    -------
    int
        Número de rounds (log2(qtd_players)). Se qtd_players não for suportado,
        a função imprime uma mensagem de erro e retorna -1.

    Exemplo
    -------
    qtd_players = 4
    log2(4) = 2 -> semifinal + final = 2 rounds
    """
    if not qtd_players in QTD_PLAYERS_LIMITS:
        print(
            f"A quantidade de jogadores informada não se enquadra no padrão permitido pelo sistema."
        )
        return -1
    return int(math.log2(qtd_players))


def get_next_acceptable_limit(qtd_players):
    for limit in QTD_PLAYERS_LIMITS:
        if qtd_players < limit:
            return limit
    return QTD_PLAYERS_LIMITS[-1]
