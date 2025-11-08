INSERT INTO GAMES (TITULO, DESCRICAO)
VALUES (
    'Street Fighter V',
    'Um jogo de luta popular da série Street Fighter.'
  ),
  (
    'Tekken 7',
    'Um jogo de luta em 3D com uma vasta gama de personagens.'
  ),
  (
    'Mortal Kombat 11',
    'Conhecido por sua violência gráfica e fatalities.'
  ),
  (
    'Super Smash Bros. Ultimate',
    'Um jogo de luta crossover com personagens de várias franquias.'
  ),
  (
    'Dragon Ball FighterZ',
    'Um jogo de luta baseado na popular série Dragon Ball.'
  );
-- O hash da senha abaixo corresponde a 'Type20!@#'
INSERT INTO USUARIOS (NOME_COMPLETO, NICKNAME, EMAIL, SENHA, BALANCE)
VALUES (
    'Alice Silva',
    'AliceS',
    'alice@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Bruno Costa',
    'BrunoC',
    'bruno@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Carla Mendes',
    'CarlaM',
    'carla@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Daniel Rocha',
    'DanielR',
    'daniel@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Eva Lima',
    'EvaL',
    'eva@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Felipe Santos',
    'FelipeS',
    'felipe@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Gabriela Fernandes',
    'GabrielaF',
    'gabriela@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Hugo Almeida',
    'HugoA',
    'hugo@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Isabela Nunes',
    'IsabelaN',
    'isabela@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'João Pereira',
    'JoaoP',
    'joao@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Karina Gomes',
    'KarinaG',
    'karina@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Lucas Ribeiro',
    'LucasR',
    'lucas@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Mariana Castro',
    'MarianaC',
    'mariana@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Nicolas Barros',
    'NicolasB',
    'nicolas@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  ),
  (
    'Olivia Moreira',
    'OliviaM',
    'olivia@example.com',
    '$2b$12$z0Bt1RxOl1jCGHkauMZn9Ow8o7j3NAVA0wjz7VDAJJ1B6Hy5f9z4C',
    0
  );
-- Seed Events
INSERT INTO EVENTOS (
    OWNER_ID,
    GAME_ID,
    TITULO,
    DESCRICAO,
    DATA_INICIO,
    DATA_FIM,
    QTD_PLAYERS,
    VALOR_RECOMPENSA
  )
VALUES (
    1,
    1,
    'Torneio Street Fighter V - Iniciante',
    'Torneio para jogadores iniciantes de Street Fighter V.',
    '2025-08-01',
    '2025-08-07',
    8,
    100.00
  );
-- Seed Event Tickets
INSERT INTO EVENTOS_TICKETS (EVENTO_ID, USUARIO_ID)
VALUES (1, 2),
  (1, 3),
  (1, 4),
  (1, 5),
  (1, 6),
  (1, 7),
  (1, 8);