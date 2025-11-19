def get_safe_int(prompt: str):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print('Digite um valor inteiro válido!')

def to_float(value: str):
     try:
         return float(value)
     except:
         print('Digite um valor float válido!')