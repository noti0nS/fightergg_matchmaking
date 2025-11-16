from data import eventos
from utils import type_utils, ui_utils, events_utils


def select_event_from_user(usuario_id):
    try:
        usuario_eventos = eventos.fetch_active_events_by_user(usuario_id)
        if len(usuario_eventos) == 0:
            print(
                "Não foi possível encontrar nenhum evento ativo para o usuário logado."
            )
            return None

        for usuario_evento in usuario_eventos:
            _display_event_card(usuario_evento)

        while True:
            event_id = type_utils.get_safe_int(
                "Informe o ID do evento que você deseja gerenciar: "
            )
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
    qtd_participantes = usuario_evento[8]
    qtd_players = usuario_evento[7]
    print(
        f"""[{usuario_evento[0]}] · {usuario_evento[1]}
{usuario_evento[2]}

Inscrições: {usuario_evento[3]} até {usuario_evento[4]}
Recompensa: {usuario_evento[6]} \t\t\t Participantes: {qtd_participantes}/{qtd_players} {'(FULL)' if qtd_players == qtd_participantes else ''}
Game: {usuario_evento[9]}
Em andamento: {'SIM' if usuario_evento[5] else 'NÃO'}
--------------------------------------------------------------------------"""
    )


def start_event(usuario_evento) -> bool:
    qtd_players = usuario_evento[7]
    qtd_participantes = usuario_evento[8]

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

    return eventos.activate_event(usuario_evento[0])


def manage_event_matches(evento_id):
    leave = False
    render_menu = True

    while not leave:
        evento_data = eventos.fetch_event_headline(evento_id)
        matches_data = eventos.fetch_event_matches(evento_id)
        current_round = _get_current_round(matches_data)

        print(
            f"""
{'*' * 50}
{evento_data[0]}
GAME: {evento_data[2]}
RECOMPENSA: R$ {evento_data[1]}
ROUND: {current_round}
{'*' * 50}"""
        )

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

            print()

            match option:
                case 1:
                    # TODO: _set_match_winner_submenu()
                    break
                case 2:
                    if _set_match_round_submenu(matches_data[current_round - 1]):
                        break
                    render_menu = True
                case 3:
                    leave = True
                    break

            print()

        render_menu = True
        ui_utils.clear_console()


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
    "(VENCEDOR)" if player_id == winner_id else ""


def _set_match_round_submenu(matches: list):
    match_id = type_utils.get_safe_int("Selecione o ID da partida: ")
    current_match_round = next((m[6] for m in matches if m[0] == match_id), None)
    if not current_match_round:
        print(f"A partida '{match_id}' não está disponível para seleção.")
        return False
    return eventos.increment_match_round(match_id, current_match_round)
