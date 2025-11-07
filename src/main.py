from dotenv import load_dotenv
from infra import db

def main():
    load_dotenv() # Carrega variáveis de ambiente do arquivo .env
    
    print("Hello, World!")

if __name__ == "__main__":
    main()