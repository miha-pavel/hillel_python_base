drop_database_query = "DROP DATABASE IF EXISTS hillel_postgres_lesson;"

create_database_query = "CREATE DATABASE hillel_postgres_lesson;"

create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL, 
        age INTEGER,
        gender TEXT,
        nationality TEXT
    );
"""

create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
        id SERIAL PRIMARY KEY, 
        title TEXT NOT NULL, 
        description TEXT NOT NULL, 
        user_id INTEGER NOT NULL REFERENCES users(id)
    );
"""

create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY, 
        user_id INTEGER NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES users (id),
        post_id integer NOT NULL, 
        FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
        id SERIAL PRIMARY KEY, 
        text TEXT NOT NULL, 
        user_id INTEGER NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES users (id),
        post_id INTEGER NOT NULL, 
        FOREIGN KEY (post_id) REFERENCES posts (id)
    );
"""

def insert_user_query(user_records):
    return f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records};"

def insert_post_query(post_records):
    return f"INSERT INTO posts (title, description, user_id) VALUES {post_records};"

create_comments = """
    INSERT INTO
        comments (text, user_id, post_id)
    VALUES
        ('Count me in', 1, 6),
        ('What sort of help?', 5, 3),
        ('Congrats buddy', 2, 4),
        ('I was rooting for Nadal though', 4, 5),
        ('Help with your thesis?', 2, 3),
        ('Many congratulations', 5, 4);
"""
CREATE TABLE IF NOT EXISTS rec_phones (
    id SERIAL PRIMARY KEY,
    length INTEGER,
    text TEXT NOT NULL,
    sentiment TEXT NOT NULL);
create_query = f"""
    INSERT INTO
        rec_phones (length, text, sentiment)
    VALUES
        ({length}, {text}, {json});
"""

insert_likes_query = "INSERT INTO likes ( user_id, post_id ) VALUES ( %s, %s );"

# Выбераем все записи из таблицы users:
select_users = "SELECT * FROM users;"

# Вы также можете выполнять более сложные запросы,
# включающие операции типа JOIN для извлечения данных из двух связанных таблиц.
# Например, следующий скрипт возвращает идентификаторы и имена пользователей,
# а также описание сообщений, опубликованных этими пользователями:
select_users_posts = """
    SELECT
        users.id,
        users.name,
        posts.description
    FROM
        posts
    INNER JOIN users ON users.id = posts.user_id;
"""

select_posts_comments_users = """
    SELECT
        posts.description as post,
        text as comment,
        name
    FROM
        posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN users ON users.id = comments.user_id
"""

# В качестве примера обновим текст поста с id равным 2. Сначала создадим описание для SELECT:
select_post_description = "SELECT description FROM posts WHERE id = 2;"

# Следующий скрипт обновит описание:
update_post_description = """
    UPDATE
        posts
    SET
        description = 'The weather has become pleasant now'
    WHERE
        id = 2;
"""

delete_comment = "DELETE FROM comments WHERE id = 5;"
