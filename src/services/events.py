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
            if not event_id:
                continue
            # event_id = int(input("Informe o ID do evento que você deseja gerenciar: "))
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
                f"O evento possui {qtd_participantes} jogadores inscritos, o que impossibilita o duelo entre todos. Não é possível prosseguir com a operação."
            )
            return False

    return eventos.start_event(usuario_evento[0])
