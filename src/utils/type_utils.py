def get_safe_int(prompt: str):
    try:
        value = int(input(prompt))
        return value
    except:
        print('Digite um valor inteiro válido!')