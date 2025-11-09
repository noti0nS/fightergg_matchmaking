from utils import validators_utils, password_utils
from data import user

def login(email: str, password: str) -> bool:
    try:
        if not validators_utils.is_email_valid(email):
            print("O E-mail fornecido é inválido.")
            return False

        password_status = validators_utils.get_password_status(password)
        if password_status:
            print(f"A senha fornecida é inválida: {password_status}")
            return False

        user_password = user.fetch_user_password(email)
        return password_utils.verify_password(password, user_password)
    except Exception as e:
        print(e)
        return False
    

def register(nome_completo: str, nickname: str, email: str, password: str) -> bool:
    #Registra um novo usuario no sistema
    try: 
        #Validar E-mail
        if not validators_utils.is_email_valid(email):
            print(f"O e-mail fornecido é inválido: {email}")
            return False
        
        #Validar Formato da Senha
        password_status = validators_utils.get_password_status(password)
        if password_status:
            print(f"A senha fornecida é invalida: {password_status}")
            return False
        
        #Validar erros
        if user.check_email_exists(email):
            print("Erro: Este e-mail já está cadastrado")
            return False

        if user.check_nickname_exists(nickname):
            print("Erro: Este e-mail já está cadastrado")
            return False
        
        #Criptografia de senha
        hashed_password = password_utils.hash_password(password)
        success = user.create_user(
            nome_completo=nome_completo,
            nickname=nickname,
            email=email,
            senha_hash=hashed_password 
        )
        if success:
            print(f"Usuário '{nickname}' registrado com sucesso!")
            return True
        else:
            print("Ocorreu um erro ao registrar o usuário no banco de dados.")
            return False

    except Exception as e:
        print(f"Um erro inesperado ocorreu durante o registro: {e}")
        return False

