CREATE TABLE IF NOT EXISTS mainmenu(
    id integer PRIMARY KEY AUTOINCREMENT, 
    title text NOT NULL,
    url text NOT NULL
);

INSERT INTO mainmenu(id, title, url) VALUES (1, 'Главная', '/');
INSERT INTO mainmenu(id, title, url) VALUES (2, 'Добавить статью', '/add_post');
INSERT INTO mainmenu(id, title, url) VALUES (3, 'О нас', '/about');
INSERT INTO mainmenu(id, title, url) VALUES (4, 'Контакт', '/contact');
INSERT INTO mainmenu(id, title, url) VALUES (5, 'Вход', '/login');

CREATE TABLE IF NOT EXISTS posts(
    id integer PRIMARY KEY AUTOINCREMENT, 
    title text NOT NULL,
    text text NOT NULL,
    time integer NOT NULL
);

-- SELECT * FROM mainmenu;