from data import eventos_data, games_data
from utils import type_utils, ui_utils, events_utils

import dateparser, datetime


def select_event_from_user(usuario_id):
    try:
        usuario_eventos = eventos_data.fetch_active_events_by_user(usuario_id)
        if len(usuario_eventos) == 0:
            print(
                "Não foi possível encontrar nenhum evento ativo para o usuário logado."
            )
            return

        for usuario_evento in usuario_eventos:
            _display_event_card(usuario_evento)

        while True:
            event_id = type_utils.get_safe_int(
                "Informe o ID do evento que você deseja gerenciar (-1 para sair): "
            )
            if event_id == -1:
                return
            found_event = next(
                (ue for ue in usuario_eventos if ue[0] == event_id), None
            )
            if found_event:
                return found_event
            print(
                f"Não foi possível encontrar o evento com ID {event_id}. Tente novamente."
            )

    except Exception as e:
        print(e)


def _display_event_card(usuario_evento):
    qtd_participantes = usuario_evento[7]
    qtd_players = usuario_evento[6]
    print(
        f"""[{usuario_evento[0]}] · {usuario_evento[1]}
{usuario_evento[2]}

Data do Evento: {usuario_evento[3]} até {usuario_evento[4]}
Recompensa: {usuario_evento[5]} \t\t\t Participantes: {qtd_participantes}/{qtd_players} {'(FULL)' if qtd_players == qtd_participantes else ''}
Game: {usuario_evento[8]}
Em andamento: {'SIM' if usuario_evento[4] else 'NÃO'}
--------------------------------------------------------------------------"""
    )


def start_event(usuario_evento) -> bool:
    qtd_players = usuario_evento[6]
    qtd_participantes = usuario_evento[7]

    if qtd_players > qtd_participantes:
        acceptable_qtd_players = events_utils.get_next_acceptable_limit(
            qtd_participantes
        )
        if qtd_participantes == acceptable_qtd_players:
            print(
                f"O evento possui {qtd_participantes} jogadores inscritos de um limite de {qtd_players}. Deseja prosseguir mesmo assim?"
            )
            print("[1] - SIM")
            print("[2] - NÃO")
            while True:
                option = ui_utils.get_menu_option("> ")
                if option == 1:
                    break
                elif option == 2:
                    return False

        else:
            print(
                f"O evento possui {qtd_participantes} jogadores inscritos, o que impossibilita o duelo entre todos. Você precisa ter ao menos {acceptable_qtd_players} jogadores registrados para prosseguir."
            )
            return False

    return eventos_data.activate_event(usuario_evento[0])


def manage_event_matches(evento_id):
    leave = False
    render_menu = True
    while not leave:
        evento_data = eventos_data.fetch_event_headline(evento_id)
        if evento_data[3]:
            _display_event_headline(evento_data)
            break

        matches_data = eventos_data.fetch_event_matches(evento_id)
        current_round = _get_current_round(matches_data)

        _display_event_headline(evento_data, current_round)
        _display_event_matches(matches_data, current_round)

        while True:
            if render_menu:
                print("[1] - Definir vencedor")
                print("[2] - Avançar round")
                print("[3] - Voltar ao menu de Eventos")

            option = ui_utils.get_menu_option("> ", 1, 3)
            if option == -1:
                render_menu = False
                continue
            elif option == 3:
                leave = True
                break

            render_menu = True

            ui_utils.divider()

            match_id = type_utils.get_safe_int("Selecione o ID da partida: ")
            matches = matches_data[current_round - 1]
            match = next(
                (m for m in matches if m[0] == match_id),
                None,
            )
            if not match:
                print(f"A partida '{match_id}' não está disponível para seleção.")
                ui_utils.divider()
                continue

            match option:
                case 1:
                    ui_utils.divider()
                    if _set_match_winner_submenu(match):
                        break
                case 2:
                    if eventos_data.increment_match_round(match_id):
                        break
            print()

        ui_utils.clear_console()


def _display_event_headline(evento_data, current_round=None):
    print(
        f"""
{'*' * 50}
{evento_data[0]}
GAME: {evento_data[2]}
RECOMPENSA: R$ {evento_data[1]}
{f'ROUND: {current_round}' if current_round else ''} \t\t {f'VENCEDOR: {evento_data[3]}' if evento_data[3] else ''}
{'*' * 50}"""
    )


def _get_current_round(matches_data):
    for i in range(len(matches_data)):
        # verifica se nas partidas do round atual (i + 1) há alguma em que não há vencedor definido.
        any_match_is_happening = any((not m[3] for m in matches_data[i]))
        if any_match_is_happening:
            return i + 1
    return -1  # all rounds are done


def _display_event_matches(matches_data: list[list], current_round: int):
    rounds_to_display = len(matches_data) - (len(matches_data) - current_round)
    for i in range(rounds_to_display):
        ui_utils.pretty_message(f"ROUND {i + 1}")
        for match in matches_data[i]:
            winner_id = match[3]
            if winner_id:
                print(
                    f"""{match[7]} {_show_winner_text(match[1], winner_id)} x {match[8]} {_show_winner_text(match[2], winner_id)} 
ROUND NA PARTIDA: {match[6]}
"""
                )
            else:
                print(
                    f"""[{match[0]}] {match[7]} x {match[8]}
ROUND NA PARTIDA: {match[6]}
"""
                )


def _show_winner_text(player_id, winner_id):
    return "(VENCEDOR)" if player_id == winner_id else ""


def _set_match_winner_submenu(match):
    print(f"[1] - {match[7]}")
    print(f"[2] - {match[8]}")
    print(f"[3] - Voltar\n")
    print("Quem foi o vencedor da partida?")

    winner_id = None
    while not winner_id:
        option = ui_utils.get_menu_option("> ", 1, 3)
        if option == -1:
            continue
        elif option == 3:
            return False
        winner_id = match[option]

    return eventos_data.set_match_winner(match[0], winner_id)


def create_event(user_id):
    new_event = {}

    new_event["owner_id"] = user_id

    valid = False
    while not valid:
        titulo = input("Título do Evento: ").strip()
        if len(titulo) == 0:
            ui_utils.pretty_message("O título não pode ser vazio!")
            continue
        new_event["titulo"] = titulo
        valid = True

    valid = False
    while not valid:
        input_date = input("Data do Evento (YYYY-MM-DD): ").strip()
        data_evento = dateparser.parse(input_date)
        if not data_evento:
            ui_utils.pretty_message(f"A data '{input_date}' não é válida!")
            continue
        today = datetime.date.today()
        if data_evento.date() < today:
            ui_utils.pretty_message(
                f"Você precisa informar uma data igual ou posterior a data atual ({today})!"
            )
            continue
        new_event["data_inscr"] = data_evento
        valid = True

    new_event["descricao"] = input("Descrição do Evento: ").strip()

    games = games_data.get_all_games()
    for game in games:
        print(f"[{game[0]}] - {game[1]}\n{game[2]}\n")

    valid = False
    while not valid:
        game_id = type_utils.get_safe_int(input("Digite o ID do game do evento: "))
        if not any((g[0] == game_id for g in games)):
            ui_utils.pretty_message(
                f"O ID não existe '{game_id}' não existe na tabela de games."
            )
            continue
        new_event["game_id"] = game_id
        valid = True

    print("↓ Quantida de jogadores suportada no sistema ↓")
    for qtd_player_limit in events_utils.QTD_PLAYERS_LIMITS:
        print(qtd_player_limit)

    valid = False
    while not valid:
        qtd_players = type_utils.get_safe_int(
            input("Digite a quantidade de jogadores para o seu evento: ")
        )
        if not qtd_players in events_utils.QTD_PLAYERS_LIMITS:
            ui_utils.pretty_message(
                "A quantidade de jogadores digitada não é suportada."
            )
            continue
        new_event["qtd_players"] = qtd_players
        valid = True

    return eventos_data.create_event(new_event)


def edit_event_info(selected_event) -> bool:
    id_evento = selected_event[0]
    titulo = selected_event[1]

    # Mostra o evento que será editado
    ui_utils.clear_console()

    # Lista/tupla
    print(f"Editando o evento: {titulo} (ID: {id_evento})")

    # Pede novos dados ao usuário
    novo_titulo = input("Novo nome (ENTER para manter): ").strip()
    nova_descricao = input("Nova descrição (ENTER para manter): ").strip()
    novo_valor_recompensa = input(
        "Novo valor de recompensa (ENTER para manter): "
    ).strip()

    # Cria o novo evento, mantendo valores antigos se o usuário não fornecer novos
    updated_event = {
        "id": id_evento,
        "titulo": novo_titulo if novo_titulo else titulo,
        "descricao": nova_descricao if nova_descricao else selected_event[2],
        "valor_recompensa": (
            float(novo_valor_recompensa) if novo_valor_recompensa else selected_event[5]
        ),
    }
    # Chama a atualização no banco de dados
    sucesso = eventos_data.update_event(updated_event)

    if sucesso:
        print("Evento atualizado com sucesso!")
    else:
        print("Erro ao atualizar o evento.")

    return sucesso
