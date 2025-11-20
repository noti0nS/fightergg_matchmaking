from dotenv import load_dotenv
from utils import ui_utils
from services import auth_service, eventos_service


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
                user = auth_service.login()
            case 2:
                if auth_service.register():
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
            print("[6] - Exibir Dados Pessoais")
            print("[7] - Logout")

            option = ui_utils.get_menu_option("> ", 1, 7)
            if option == -1:
                continue

            ui_utils.clear_console()

            match option:
                case 1:
                    if _join_event_submenu(user):
                        ui_utils.clear_console()
                        ui_utils.pretty_message(
                            "Você está participando do evento selecionado!"
                        )
                case 2:
                    _show_events_joined_submenu(user)
                case 3:
                    _manage_events_submenu(user)
                case 4:
                    if _create_event_submenu(user):
                        ui_utils.clear_console()
                        ui_utils.pretty_message("Evento criado com sucesso!")
                case 5:
                    if _remove_event_submenu(user):
                        ui_utils.clear_console()
                        ui_utils.pretty_message("Evento removido com sucesso!")
                case 6:
                    auth_service.show_personal_info(user[0])
                case 7:
                    user = None

            ui_utils.divider()

        ui_utils.show_banner()

    print("Até breve! :-)")


def _join_event_submenu(user):
    ui_utils.pretty_message("PARTICIPAR DE EVENTOS")
    return eventos_service.create_event_ticket(user[0])


def _show_events_joined_submenu(user):
    ui_utils.pretty_message(f"EVENTOS QUE {user[1]} ESTÁ PARTICIPANDO")
    eventos_service.show_event_progress(user[0])


def _manage_events_submenu(user):
    ui_utils.pretty_message("GERENCIAMENTO DE EVENTOS")
    selected_event = eventos_service.select_event_from_user(user[0])
    if not selected_event:
        return
    ui_utils.clear_console()
    ui_utils.pretty_message(f"O que deseja fazer com o evento '{selected_event[1]}'?")

    em_andamento: bool = selected_event[4]
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
                    eventos_service.manage_event_matches(selected_event[0])
                    ui_utils.divider()
                case 2:
                    ui_utils.show_banner()
                    break
        else:
            match option:
                case 1:
                    em_andamento = eventos_service.start_event(selected_event)
                    if em_andamento:
                        ui_utils.clear_console()
                        msg = f"O EVENTO '{selected_event[1]}' COMEÇOU!"
                        ui_utils.pretty_message(msg)
                    else:
                        ui_utils.divider()
                case 2:
                    ui_utils.clear_console()
                    if eventos_service.edit_event_info(selected_event):
                        ui_utils.clear_console()
                    else:
                        ui_utils.divider()
                case 3:
                    ui_utils.show_banner()
                    break


def _create_event_submenu(user):
    ui_utils.pretty_message("CRIAR NOVO EVENTO")
    return eventos_service.create_event(user[0])


def _remove_event_submenu(user):
    ui_utils.pretty_message("EXCLUIR EVENTO")
    return eventos_service.delete_event(user[0])


if __name__ == "__main__":
    main()
