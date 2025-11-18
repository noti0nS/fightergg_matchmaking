from utils import validators_utils, password_utils
from data import usuarios

import getpass


def login() -> tuple | None:
    try:
        email = input("Digite o seu e-mail: ")
        password = getpass.getpass("Digite a sua senha: ")

        if not validators_utils.is_email_valid(email):
            print(
                "As credencias estão inválidas! Verifique se o e-mail e a senha foram digitados corretamente."
            )
            return None

        password_strength_result = validators_utils.validate_password_strength(password)
        if password_strength_result:
            print(password_strength_result)
            return None

        user = usuarios.get_user_by_email(email)
        if not password_utils.verify_password(password, user[2]):
            print(
                "As credencias estão inválidas! Verifique se o e-mail e a senha foram digitados corretamente."
            )
            return None

        return (user[0], user[1])  # Retorna apenas o id e nickname.
    except Exception as e:
        print(e)


def register() -> bool:
    # Registra um novo usuario no sistema
    try:

        nome_completo = input("Digite seu nome completo: ")
        nickname = input("Escolha um nickname: ")
        email = input("Digite seu e-mail: ")
        password = getpass.getpass("Escolha uma senha: ")

        # Validar E-mail
        if not validators_utils.is_email_valid(email):
            print(f"O e-mail fornecido é inválido: {email}")
            return False

        # Validar Formato da Senha
        password_status = validators_utils.validate_password_strength(password)
        if password_status:
            print(password_status)
            return False

        # Validação de erros de email e nick
        if usuarios.check_email_exists(email):
            print("Erro: Este e-mail já está cadastrado")
            return False

        if usuarios.check_nickname_exists(nickname):
            print("Erro: Nickname já está em uso")
            return False

        # Criptografia de senha, em hash
        hashed_password = password_utils.generate_hashed_password(password)
        return usuarios.create_user(nome_completo, nickname, email, hashed_password)

    except Exception as e:
        print(f"Um erro inesperado ocorreu durante o registro: {e}")
        return False


def show_personal_info(usuario_id):
    user_info = usuarios.get_user_info(usuario_id)
    if not user_info:
        print("Não foi possível encontrar informações para o Usuário logado.")
        return
    print(f"""
Nome Completo: {user_info[0]}
Email: {user_info[1]}
Nickname: {user_info[2]}
Saldo: R$ {user_info[3]}""")
