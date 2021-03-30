# Lля PostgreSQL в стандартной библиотеке Python нет модуля для взаимодействия с базой данных.
# Но и для этой задачи есть решение – модуль psycopg2
from psycopg2 import connect, OperationalError


# Определим функцию create_connection() для подключения к базе данных PostgreSQL:
def create_connection(db_name, db_user, db_host, db_port, db_password):
    connection = None
    try:
        # Подключение осуществляется через интерфейс psycopg2.connect()
        connection = connect(
            database=db_name,
            user=db_user,
            host=db_host,
            password=db_password,
            port=db_port,
        )
        # autocommit = True гарантирует, что psycopg выполнит каждый оператор и немедленно зафиксирует его.
        connection.autocommit = True
        print(f"Connection to PostgreSQL DB {db_name} successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    # connection.autocommit = True
    # Для выполнения запросов используется объект cursor.
    # https://www.psycopg.org/docs/cursor.html
    cursor = connection.cursor()
    try:
        # Для выполнения запросов в PostgresQL используется метод cursor.execute().
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()  #fetchall() возвращает список кортежей, где каждый кортеж сопоставлен с соответствующей строкой в ​​извлеченных записях.
    except Error as e:
        print(f"The error '{e}' occurred")
    return result


def close_connection(connection):
    connection.close()
    print("The connection with postgresql database was closed")


if __name__ == "__main__":
    # 2. ПОДКЛЮЧЕНИЕ К БАЗАМ ДАННЫХ
    connection = create_connection(
        db_name="postgres",
        db_user="postgres",
        db_host="127.0.0.1",
        db_port="5433",
        db_password='345',
        )
    drop_database_query = "DROP DATABASE IF EXISTS hillel_postgres_lesson;"
    execute_query(connection, drop_database_query)
    # Теперь внутри дефолтной БД postgres нужно создать базу данных hillel_postgres_lesson.
    create_database_query = "CREATE DATABASE hillel_postgres_lesson;"
    execute_query(connection, create_database_query)
    connection = create_connection(
        db_name="hillel_postgres_lesson",
        db_user="postgres",
        db_host="127.0.0.1",
        db_port="5433",
        db_password='345',
        )

    # 3. СОЗДАНИЕ ТАБЛИЦ
    create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL, 
            age INTEGER,
            gender TEXT,
            nationality TEXT
        );
    """
    execute_query(connection, create_users_table)
    
    create_posts_table = """
        CREATE TABLE IF NOT EXISTS posts(
            id SERIAL PRIMARY KEY, 
            title TEXT NOT NULL, 
            description TEXT NOT NULL, 
            user_id INTEGER NOT NULL REFERENCES users(id)
        );
    """
    execute_query(connection, create_posts_table)

    create_likes_table = """
        CREATE TABLE IF NOT EXISTS likes (
            id SERIAL PRIMARY KEY, 
            user_id INTEGER NOT NULL, 
            FOREIGN KEY (user_id) REFERENCES users (id),
            post_id integer NOT NULL, 
            FOREIGN KEY (post_id) REFERENCES posts (id)
        );
    """
    execute_query(connection, create_likes_table) 

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
    execute_query(connection, create_comments_table)

    # 4. ВСТАВКА ЗАПИСЕЙ
    users = [
        ("James", 25, "male", "USA"),
        ("Leila", 32, "female", "France"),
        ("Brigitte", 35, "female", "England"),
        ("Mike", 40, "male", "Denmark"),
        ("Elizabeth", 21, "female", "Canada"),
    ]
    user_records = ", ".join(["%s"] * len(users))
    insert_query = f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records};"
    cursor = connection.cursor()
    cursor.execute(insert_query, users)

    posts = [
        ("Happy", "I am feeling very happy today", 1),
        ("Hot Weather", "The weather is very hot today", 2),
        ("Help", "I need some help with my work", 2),
        ("Great News", "I am getting married", 1),
        ("Interesting Game", "It was a fantastic game of tennis", 5),
        ("Party", "Anyone up for a late-night party today?", 3),
    ]
    post_records = ", ".join(["%s"] * len(posts))
    insert_query = f"INSERT INTO posts (title, description, user_id) VALUES {post_records};"
    cursor = connection.cursor()
    cursor.execute(insert_query, posts)

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
    execute_query(connection, create_comments)

    # Второй подход использует метод cursor.executemany(), который принимает два параметра:
        # 1. Строка query, содержащая заполнители для вставляемых записей.
        # 2. Список записей, которые мы хотим вставить.
    sql = "INSERT INTO likes ( user_id, post_id ) VALUES ( %s, %s );"
    val = [(4, 5), (3, 4)]
    cursor = connection.cursor()
    cursor.executemany(sql, val)  
    connection.commit()

    # # 5. ИЗВЛЕЧЕНИЕ ДАННЫХ ИЗ ЗАПИСЕЙ
    # # Выбераем все записи из таблицы users:
    # select_users = "SELECT * FROM posts;"
    # users = execute_read_query(connection, select_users)
    # print('users: ', users)
    # for user in users:
    #     print(user)
    # print('+++++++++++++++++++++++++++++++++++++++++++==')

    # # Вы также можете выполнять более сложные запросы,
    # # включающие операции типа JOIN для извлечения данных из двух связанных таблиц.
    # # Например, следующий скрипт возвращает идентификаторы и имена пользователей,
    # # а также описание сообщений, опубликованных этими пользователями:
    # select_users_posts = """
    #     SELECT
    #         users.id,
    #         users.name,
    #         posts.description
    #     FROM
    #         posts
    #     INNER JOIN users ON users.id = posts.user_id
    # """
    # users_posts = execute_read_query(connection, select_users_posts)
    # for users_post in users_posts:
    #     print(users_post)

    # # Следующий скрипт возвращает все сообщения вместе с комментариями к сообщениям и именами пользователей, которые разместили комментарии:
    # select_posts_comments_users = """
    #     SELECT
    #         posts.description as post,
    #         text as comment,
    #         name
    #     FROM
    #         posts
    #     INNER JOIN comments ON posts.id = comments.post_id
    #     INNER JOIN users ON users.id = comments.user_id
    # """
    # posts_comments_users = execute_read_query(
    #     connection, select_posts_comments_users
    # )
    # for posts_comments_user in posts_comments_users:
    #     print(posts_comments_user)

    # # Чтобы вернуть имена столбцов, нужно забрать атрибут description объекта cursor.
    # cursor = connection.cursor()
    # cursor.execute(select_posts_comments_users)
    # cursor.fetchall()
    # column_names = [description[0] for description in cursor.description]
    # print(column_names)


    # 6. ОБНОВЛЕНИЕ ЗАПИСЕЙ ТАБЛИЦЫ
    # В качестве примера обновим текст поста с id равным 2. Сначала создадим описание для SELECT:
    select_post_description = "SELECT description FROM posts WHERE id = 2;"
    post_description = execute_read_query(connection, select_post_description)
    for description in post_description:
        print(description)

    # Следующий скрипт обновит описание:
    update_post_description = """
        UPDATE
        posts
        SET
        description = 'The weather has become pleasant now'
        WHERE
        id = 2;
    """
    execute_query(connection, update_post_description)

    # Теперь, если мы выполним SELECT-запрос еще раз, увидим следующий результат:
    post_description = execute_read_query(connection, select_post_description)
    for description in post_description:
        print(description)

    # 7. УДАЛЕНИЕ ЗАПИСЕЙ ТАБЛИЦЫ
    delete_comment = "DELETE FROM comments WHERE id = 5;"
    execute_query(connection, delete_comment)

    # 8. ЗАКРЫВАЕМ КОННЭКШИН С БАЗОЙ И УДОЛЯЕМ КАСТОМНУЮ БАЗУ
    close_connection(connection)
    connection = create_connection(
        db_name="postgres",
        db_user="postgres",
        db_host="127.0.0.1",
        db_port="5433",
        db_password='345',
    )
    drop_database_query = "DROP DATABASE hillel_postgres_lesson;"
    execute_query(connection, drop_database_query)
    close_connection(connection)
