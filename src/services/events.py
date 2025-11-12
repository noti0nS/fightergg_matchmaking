from data import eventos
from utils import type_utils


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
    print(
        f"""[{usuario_evento[0]}] · {usuario_evento[1]}
{usuario_evento[2]}

Inscrições começam em {usuario_evento[3]} e vão até {usuario_evento[4]}
Em andamento: {'SIM' if [usuario_evento[5]] else 'NÃO'}
Recompensa: {usuario_evento[6]} \t\t\t Participantes: {usuario_evento[8]}/{usuario_evento[7]}
--------------------------------------------------------------------------"""
    )
