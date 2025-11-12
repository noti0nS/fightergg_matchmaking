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

        user: tuple = None
        match option:
            case 1:
                ui_utils.clear_console()
                user = auth.login()
            case 2:
                ui_utils.clear_console()
                auth.register()
            case 3:
                break

        if not user:
            continue

        ui_utils.show_banner()

        print(f"Seja bem vindo, {user[1]}!\n")

        while user:
            print("[1] - Listar Eventos")
            print("[2] - Participar de Eventos")
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
                    _list_events_submenu(user)
                case 2:
                    _join_event_submenu(user)
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


def _list_events_submenu(user):
    """
    TODO Gabriel: Implementar Listagem de Eventos
    """


def _join_event_submenu(user):
    """
    TODO Gabriel: Implementar Participar de Eventos
    """


def _manage_events_submenu(user):
    print("GERENCIAMENTO DE EVENTOS")

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

        if em_andamento:
            match option:
                case 1:
                    # TODO: _manage_matches()
                    pass
                case 2:
                    ui_utils.show_banner()
                    break
        else:
            match option:
                case 1:
                    # TODO _start_event()
                    pass
                case 2:
                    # TODO GABRIEL: _edit_event_info()
                    pass
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
