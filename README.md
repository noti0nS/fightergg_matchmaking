# FighterGG - Gerenciador de Torneios de Luta

FighterGG é um sistema de linha de comando (CLI) projetado para gerenciar eventos e torneios de jogos de luta. Ele permite que os usuários se cadastrem, criem e participem de torneios, acompanhem partidas e muito mais.

Este projeto foi desenvolvido como parte da avaliação da disciplina de **Laboratório de Programação II**.

## Features

- **Autenticação de Usuários:** Sistema de login e cadastro seguro.
- **Gerenciamento de Eventos:** Crie, liste, gerencie e exclua seus próprios torneios.
- **Participação em Torneios:** Inscreva-se em eventos criados pela comunidade.
- **Visualização de Informações:** Liste todos os eventos disponíveis, em andamento e finalizados.
- **Ambiente Robusto:** Utiliza um banco de dados relacional para garantir a integridade dos dados.

## Tecnologias

- **Linguagem:** Python 3
- **Banco de Dados:** PostgreSQL
- **Bibliotecas Principais:**
  - `psycopg2`: Driver para conexão com o banco de dados PostgreSQL.
  - `python-dotenv`: Gerenciamento de variáveis de ambiente para configuração segura.
  - `bcrypt`: Hashing de senhas para armazenamento seguro das credenciais dos usuários.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento local.

**1. Pré-requisitos:**
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Um servidor [PostgreSQL](https://www.postgresql.org/download/) ativo.

**2. Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/fightergg_matchmaking.git
cd fightergg_matchmaking
```

**3. Configure as Variáveis de Ambiente**
- Navegue até a pasta `src`.
- Crie uma cópia do arquivo `.env.example` e renomeie para `.env`.
- Abra o arquivo `.env` e preencha com as suas credenciais do PostgreSQL:
  ```ini
  DB_NAME=seu_banco_de_dados
  DB_USER=seu_usuario
  DB_PASSWORD=sua_senha
  DB_HOST=localhost
  DB_PORT=5432
  ```

**4. Crie um Ambiente Virtual e Instale as Dependências**
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate

# Ative o ambiente (Linux/macOS)
source venv/bin/activate

# Instale as dependências
pip install -r src/requirements.txt
```

**5. Configure o Banco de Dados**
- Conecte-se ao seu servidor PostgreSQL.
- Crie um novo banco de dados com o mesmo nome que você definiu em `DB_NAME` no arquivo `.env`.
- Execute os scripts SQL para criar a estrutura de tabelas e, opcionalmente, popular o banco com dados de exemplo. Você pode usar uma ferramenta como DBeaver, pgAdmin ou o próprio `psql`.
  - **Estrutura:** Execute o conteúdo de `src/data/sql/ddl.sql`.
  - **Dados Iniciais (Opcional):** Execute o conteúdo de `src/data/sql/seed.sql`.

**6. Execute a Aplicação**
Após configurar tudo, execute o arquivo principal para iniciar o sistema.

```bash
python src/main.py
```
O menu interativo será exibido no seu terminal.

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.
