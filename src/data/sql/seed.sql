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
INSERT INTO EVENTOS (
    OWNER_ID,
    GAME_ID,
    WINNER_ID,
    TITULO,
    DESCRICAO,
    DATA_INICIO,
    DATA_FIM,
    QTD_PLAYERS,
    VALOR_RECOMPENSA
  )
VALUES (
    2,
    2,
    5,
    'Tekken 7 King of the Iron Fist - Edição Brasil',
    'Campeonato nacional de Tekken 7. Vagas limitadas.',
    '2025-09-15',
    '2025-09-20',
    8,
    500.00
  ),
  (
    3,
    3,
    1,
    'Mortal Kombat 11 - Duelo de Fim de Semana',
    'Torneio amistoso para testar suas habilidades.',
    '2025-10-05',
    '2025-10-06',
    8,
    0.00
  ),
  (
    10,
    5,
    11,
    'Copa DBFZ - Saga de Cell',
    'Torneio temático de Dragon Ball FighterZ.',
    '2025-10-10',
    '2025-10-12',
    8,
    150.00
  ),
  (
    8,
    4,
    8,
    'Super Smash Bros. Ultimate - Batalha de Equipes',
    'Evento 2v2 de Super Smash Bros. Ultimate.',
    '2025-10-18',
    '2025-10-19',
    8,
    200.00
  ),
  (
    1,
    1,
    7,
    'Street Fighter V - Retorno do Rei',
    'Torneio de alto nível para jogadores experientes.',
    '2025-10-25',
    '2025-10-27',
    8,
    1000.00
  ),
  (
    5,
    2,
    14,
    'Tekken 7 - Desafio dos Novatos',
    'Aberto apenas para jogadores com menos de 100h de jogo.',
    '2025-11-01',
    '2025-11-02',
    8,
    50.00
  ),
  (
    4,
    4,
    NULL,
    'Smash Ultimate - Batalha Semanal de Novembro',
    'Evento semanal, venha provar que é o melhor!',
    '2025-11-08',
    '2025-11-15',
    8,
    150.00
  ),
  (
    5,
    5,
    NULL,
    'Copa DBFZ - O Despertar do Poder',
    'Quem será o guerreiro Z mais forte? Inscrições abertas.',
    '2025-12-01',
    '2025-12-05',
    8,
    200.00
  ),
  (
    1,
    1,
    NULL,
    'Street Fighter V - Torneio de Fim de Ano',
    'Fechando o ano com chave de ouro. Só para os melhores.',
    '2025-12-20',
    '2025-12-22',
    8,
    300.00
  ),
  (
    7,
    3,
    NULL,
    'Mortal Kombat 11 - Kombat League (Dezembro)',
    'Temporada de dezembro da liga online.',
    '2025-12-01',
    '2025-12-31',
    8,
    100.00
  ),
  (
    9,
    2,
    NULL,
    'Tekken 7 - O Punho de Aço',
    'Torneio relâmpago de um dia.',
    '2025-11-30',
    '2025-11-30',
    8,
    100.00
  ),
  (
    12,
    4,
    NULL,
    'Smash Ultimate - Torneio Comunitário',
    'Evento gratuito para a comunidade.',
    '2025-12-07',
    '2025-12-07',
    8,
    0.00
  ),
  (
    15,
    1,
    NULL,
    'SFV - Desafio do Ryu',
    'Torneio focado apenas em personagens Shoto.',
    '2025-12-10',
    '2025-12-11',
    8,
    50.00
  ),
  (
    11,
    5,
    NULL,
    'DBFZ - Batalha 3v3',
    'Mostre a sinergia da sua equipe.',
    '2026-01-05',
    '2026-01-07',
    8,
    250.00
  ),
  (
    6,
    3,
    NULL,
    'MK11 - Guerra de Clãs',
    'Torneio focado em times e clãs.',
    '2026-01-10',
    '2026-01-15',
    8,
    400.00
  ),
  (
    2,
    4,
    NULL,
    'Smash Ultimate - Rei da Montanha',
    'Formato King of the Hill. O vencedor leva tudo.',
    '2026-01-12',
    '2026-01-12',
    8,
    100.00
  ),
  (
    3,
    2,
    NULL,
    'Tekken 7 - Elite Showdown',
    'Apenas para jogadores ranqueados.',
    '2026-01-20',
    '2026-01-25',
    8,
    750.00
  ),
  (
    1,
    1,
    NULL,
    'Street Fighter V - Pro Tour Online (América do Sul)',
    'Etapa classificatória do Pro Tour.',
    '2026-02-01',
    '2026-02-05',
    8,
    1500.00
  ),
  (
    13,
    5,
    NULL,
    'DBFZ - Torneio do Poder',
    'Grande evento anual de Dragon Ball FighterZ.',
    '2026-02-10',
    '2026-02-15',
    8,
    2000.00
  ),
  (
    14,
    3,
    NULL,
    'Mortal Kombat 11 - Amistoso da Comunidade',
    'Evento semanal sem prêmios, apenas pela glória.',
    '2025-11-20',
    '2025-11-20',
    8,
    0.00
  ),
  (
    4,
    1,
    NULL,
    'SFV - Batalha dos Veteranos',
    'Aberto apenas para contas criadas antes de 2023.',
    '2025-11-25',
    '2025-11-26',
    8,
    100.00
  ),
  (
    8,
    2,
    NULL,
    'Tekken 7 - Duelo de Rivais',
    'Traga seu rival e resolva no ringue.',
    '2025-12-15',
    '2025-12-15',
    8,
    0.00
  ),
  (
    10,
    4,
    NULL,
    'Super Smash Bros. - A Grande Batalha',
    'Evento principal de fim de ano.',
    '2025-12-28',
    '2025-12-30',
    8,
    1200.00
  ),
  (
    12,
    5,
    NULL,
    'DBFZ - Treinamento de Inverno',
    'Torneio para praticar novas equipes e estratégias.',
    '2026-01-18',
    '2026-01-19',
    8,
    50.00
  );
INSERT INTO EVENTOS_TICKETS (EVENTO_ID, USUARIO_ID)
VALUES -- Evento 1 (Owner 1)
  (1, 2),
  (1, 3),
  (1, 4),
  (1, 5),
  (1, 6),
  (1, 7),
  (1, 8),
  (1, 9),
  -- Evento 2 (Owner 2)
  (2, 3),
  (2, 4),
  (2, 5),
  (2, 6),
  (2, 7),
  (2, 8),
  (2, 9),
  (2, 10),
  -- Evento 3 (Owner 3)
  (3, 4),
  (3, 5),
  (3, 6),
  (3, 7),
  (3, 8),
  (3, 9),
  (3, 10),
  (3, 11),
  -- Evento 4 (Owner 10)
  (4, 1),
  (4, 2),
  (4, 3),
  (4, 4),
  (4, 5),
  (4, 6),
  (4, 7),
  (4, 8),
  -- Evento 5 (Owner 8)
  (5, 1),
  (5, 2),
  (5, 3),
  (5, 4),
  (5, 5),
  (5, 6),
  (5, 7),
  (5, 9),
  -- Evento 6 (Owner 1)
  (6, 10),
  (6, 11),
  (6, 12),
  (6, 13),
  (6, 14),
  (6, 15),
  (6, 2),
  (6, 3),
  -- Evento 7 (Owner 5)
  (7, 1),
  (7, 2),
  (7, 3),
  (7, 4),
  (7, 6),
  (7, 7),
  (7, 8),
  (7, 9),
  -- Evento 8 (Owner 4)
  (8, 1),
  (8, 2),
  (8, 3),
  (8, 5),
  (8, 6),
  (8, 7),
  (8, 8),
  (8, 9),
  -- Evento 9 (Owner 5)
  (9, 6),
  (9, 7),
  (9, 8),
  (9, 9),
  (9, 10),
  (9, 11),
  (9, 12),
  (9, 13),
  -- Evento 10 (Owner 1)
  (10, 2),
  (10, 4),
  (10, 6),
  (10, 8),
  (10, 10),
  (10, 12),
  (10, 14),
  (10, 15),
  -- Evento 11 (Owner 7)
  (11, 1),
  (11, 3),
  (11, 5),
  (11, 9),
  (11, 11),
  (11, 13),
  (11, 15),
  (11, 8),
  -- Evento 12 (Owner 9)
  (12, 1),
  (12, 2),
  (12, 3),
  (12, 4),
  (12, 5),
  (12, 6),
  (12, 7),
  (12, 8),
  -- Evento 13 (Owner 12)
  (13, 1),
  (13, 2),
  (13, 3),
  (13, 4),
  (13, 5),
  (13, 6),
  (13, 7),
  (13, 8),
  -- Evento 14 (Owner 15)
  (14, 1),
  (14, 2),
  (14, 3),
  (14, 4),
  (14, 5),
  (14, 6),
  (14, 7),
  (14, 8),
  -- Evento 15 (Owner 11)
  (15, 1),
  (15, 2),
  (15, 3),
  (15, 4),
  (15, 5),
  (15, 6),
  (15, 7),
  (15, 8),
  -- Evento 16 (Owner 6)
  (16, 1),
  (16, 2),
  (16, 3),
  (16, 4),
  (16, 5),
  (16, 7),
  (16, 8),
  (16, 9),
  -- Evento 17 (Owner 2)
  (17, 1),
  (17, 3),
  (17, 4),
  (17, 5),
  (17, 6),
  (17, 7),
  (17, 8),
  (17, 9),
  -- Evento 18 (Owner 3)
  (18, 1),
  (18, 2),
  (18, 4),
  (18, 5),
  (18, 6),
  (18, 7),
  (18, 8),
  (18, 9),
  -- Evento 19 (Owner 1)
  (19, 5),
  (19, 6),
  (19, 7),
  (19, 8),
  (19, 9),
  (19, 10),
  (19, 11),
  (19, 12),
  -- Evento 20 (Owner 13)
  (20, 1),
  (20, 2),
  (20, 3),
  (20, 4),
  (20, 5),
  (20, 6),
  (20, 7),
  (20, 8),
  -- Evento 21 (Owner 14)
  (21, 1),
  (21, 2),
  (21, 3),
  (21, 4),
  (21, 5),
  (21, 6),
  (21, 7),
  (21, 8),
  -- Evento 22 (Owner 4)
  (22, 1),
  (22, 2),
  (22, 3),
  (22, 5),
  (22, 6),
  (22, 7),
  (22, 8),
  (22, 9),
  -- Evento 23 (Owner 8)
  (23, 1),
  (23, 2),
  (23, 3),
  (23, 4),
  (23, 5),
  (23, 6),
  (23, 7),
  (23, 9),
  -- Evento 24 (Owner 10)
  (24, 11),
  (24, 12),
  (24, 13),
  (24, 14),
  (24, 15),
  (24, 1),
  (24, 2),
  (24, 3),
  -- Evento 25 (Owner 12)
  (25, 1),
  (25, 3),
  (25, 5),
  (25, 7),
  (25, 9),
  (25, 11),
  (25, 13),
  (25, 15);