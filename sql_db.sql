CREATE TABLE IF NOT EXISTS mainmenu(
    id integer PRIMARY KEY AUTOINCREMENT, 
    title text NOT NULL,
    url text NOT NULL,
    fun text NOT NULL
);

INSERT INTO mainmenu(id, title, url, fun) VALUES (1, 'Главная', '/', 'index');
INSERT INTO mainmenu(id, title, url, fun) VALUES (2, 'Добавить статью', 'add_post', 'add_post');
INSERT INTO mainmenu(id, title, url, fun) VALUES (3, 'О нас', 'about', 'about');
INSERT INTO mainmenu(id, title, url, fun) VALUES (4, 'Контакт', 'contact', 'contact');
INSERT INTO mainmenu(id, title, url, fun) VALUES (5, 'Вход', 'login', 'login');

CREATE TABLE IF NOT EXISTS posts(
    id integer PRIMARY KEY AUTOINCREMENT, 
    title text NOT NULL,
    text text NOT NULL,
    time integer NOT NULL
);

-- SELECT * FROM mainmenu;