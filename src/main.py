from dotenv import load_dotenv
from ui import menu
from services import auth


def main():
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

    menu.show_banner()

    while True:
        print("1 - Realize o Login")
        print("2 - Cadastra-se")
        option = menu.get_menu_option("> ", 1, 2)
        if option == -1:
            continue

        menu.clear_console()

        user: tuple = None
        match option:
            case 1:
                email = input("Digite o seu e-mail: ")
                password = input("Digite a sua senha: ")
                user = auth.login(email, password)
            case 2:
                # TODO Gabriel: Implementar register
                pass

        while user:
            menu.clear_console()
            menu.show_banner()

            print(f"Seja bem vindo, {user[1]}!")

            input()


if __name__ == "__main__":
    main()
