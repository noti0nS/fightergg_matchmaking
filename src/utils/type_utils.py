def get_safe_int(prompt: str):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print('Digite um valor inteiro válido!')