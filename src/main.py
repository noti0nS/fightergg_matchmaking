from unittest import case
from dotenv import load_dotenv
from utils import ui_utils
from services import auth, events


def main():
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

    ui_utils.show_banner()

    while True:
        print("[1] - Realize o Login")
        print("[2] - Cadastre-se")
        print("[3] - Sair")

        option = ui_utils.get_menu_option("> ", 1, 3)
        if option == -1:
            continue

        ui_utils.clear_console()

        user: tuple = None
        match option:
            case 1:
                user = auth.login()
            case 2:
                if auth.register():
                    ui_utils.clear_console()
                    ui_utils.pretty_message("Usuário cadastrado com sucesso!")
            case 3:
                break

        if not user:
            continue

        ui_utils.show_banner()

        ui_utils.pretty_message(f"Seja bem vindo(a), {user[1]}!")

        while user:
            print("[1] - Participar de Eventos")
            print("[2] - Acompanhar Eventos")
            print("[3] - Gerenciar Eventos")
            print("[4] - Criar Evento")
            print("[5] - Excluir Evento")
            print("[6] - Logout")

            option = ui_utils.get_menu_option("> ", 1, 6)
            if option == -1:
                continue

            ui_utils.clear_console()

            match option:
                case 1:
                    _join_event_submenu(user)
                case 2:
                    _show_events_joined_submenu(user)
                case 3:
                    _manage_events_submenu(user)
                case 4:
                    _create_event_submenu(user)
                case 5:
                    _remove_event_submenu(user)
                case 6:
                    user = None

        ui_utils.show_banner()

    print("Até breve! :-)")


def _show_events_joined_submenu(user):
    ui_utils.pretty_message("LISTA DE EVENTOS ATIVOS")

    ui_utils.show_banner()

    try:
        usuario_id = user[0]  # Pega o ID do usuário
        events_list = events.fetch_active_events_by_user(
            usuario_id
        )  # Busca os eventos ativos do usuário

        if not events_list:

            print(f"\n{len(events_list)}) evento(s) ativo(s) encontrado(s):\n")
        for event in events_list:
            for evento in events_list:
                (
                    id,
                    titulo,
                    descricao,
                    data_inicio,
                    data_fim,
                    em_andamento,
                    valor_recompensa,
                    qtd_players,
                    qtd_subscribed_players,
                ) = evento

                status = "Em Andamento" if em_andamento else "Não Iniciado"
                print(f"ID: {id}")
                print(f"Título: {titulo}")
                print(f"Descrição: {descricao}")
                print(f"Data de Início das Inscrições: {data_inicio}")
                print(f"Data de Fim das Inscrições: {data_fim}")
                print(f"Status: {status}")
                print(f"Valor da Recompensa: {valor_recompensa}")
                print(f"Quantidade de Jogadores: {qtd_players}")
                print(f"Quantidade de Jogadores Inscritos: {qtd_subscribed_players}")
                print("--" * 30)

    except Exception as e:
        print(f"Ocorreu um erro ao listar os eventos: {e}")


def _join_event_submenu(user):
    ui_utils.pretty_message("PARTICIPAR DE EVENTOS")

    ui_utils.show_banner()
    try:
        usuario_id = user[0]  # Pega o ID do usuário
        events_list = events.fetch_active_events_by_user(
            usuario_id
        )  # Buscar os eventos ativos do usuário

        if not events_list:
            print(f"\n{len(events_list)} evento(s) ativo(s) encontrado(s):\n")

            for event in events_list:
                for evento in events_list:
                    (
                        id,
                        titulo,
                        descricao,
                        data_inicio,
                        data_fim,
                        em_andamento,
                        valor_recompensa,
                        qtd_players,
                        qtd_subscribed_players,
                    ) = evento

                    status = "Em Andamento" if em_andamento else "Não Iniciado"
                    print(f"ID: {id}")
                    print(f"Título: {titulo}")
                    print(f"Descrição: {descricao}")
                    print(f"Data de Início das Inscrições: {data_inicio}")
                    print(f"Data de Fim das Inscrições: {data_fim}")
                    print(f"Status: {status}")
                    print(f"Valor da Recompensa: {valor_recompensa}")
                    print(f"Quantidade de Jogadores: {qtd_players}")
                    print(
                        f"Quantidade de Jogadores Inscritos: {qtd_subscribed_players}"
                    )
                    print("--" * 30)

    except Exception as e:
        print(f"Ocorreu um erro ao listar os eventos: {e}")


def _manage_events_submenu(user):
    ui_utils.pretty_message("GERENCIAMENTO DE EVENTOS")

    selected_event = events.select_event_from_user(user[0])
    if not selected_event:
        return

    ui_utils.clear_console()

    print(f"O que deseja fazer com o evento '{selected_event[1]}'?")

    em_andamento: bool = selected_event[5]
    while True:
        if em_andamento:
            print("[1] - Gerenciar Partidas")
            print("[2] - Voltar ao Menu")
        else:
            print("[1] - Iniciar evento")
            print("[2] - Editar informações")
            print("[3] - Voltar ao Menu")

        option = ui_utils.get_menu_option("> ", 1, 2 if em_andamento else 3)
        if option == -1:
            continue

        ui_utils.clear_console()

        if em_andamento:
            match option:
                case 1:
                    events.manage_event_matches(selected_event[0])
                case 2:
                    ui_utils.show_banner()
                    break
        else:
            match option:
                case 1:
                    em_andamento = events.start_event(selected_event)
                    if em_andamento:
                        ui_utils.clear_console()
                        ui_utils.pretty_message(
                            f"O EVENTO '{selected_event[1]}' COMEÇOU!"
                        )
                case 2:
                    ui_utils.clear_console()
                    events.edit_event_info(selected_event)
                case 3:
                    ui_utils.show_banner()
                    break


def _create_event_submenu(user):
    """
    TODO Gabriel: Implementar Criação de Evento
    """


def _remove_event_submenu(user):
    """
    TODO Gabriel: Implementar remoção de evento
    P.S: Só é possível remover eventos que ainda não foram iniciados
    """


if __name__ == "__main__":
    main()
