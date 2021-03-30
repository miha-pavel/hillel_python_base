import json

import queries as qs
import utils as utl


if __name__ == "__main__":
    with open('Postgres/data.json') as f:
        data = json.load(f)
    print('data: ', data)
    # 2. ПОДКЛЮЧЕНИЕ К БАЗАМ ДАННЫХ
    con = utl.create_connection(**data['defaul_db'])
    utl.execute_query(con, qs.drop_database_query)
    # Теперь внутри дефолтной БД postgres нужно создать базу данных hillel_postgres_lesson.
    utl.execute_query(con, qs.create_database_query)
    con = utl.create_connection(**data['custom_db'])


    # 3. СОЗДАНИЕ ТАБЛИЦ
    utl.execute_query(con, qs.create_users_table)
    
    utl.execute_query(con, qs.create_posts_table)

    utl.execute_query(con, qs.create_likes_table) 

    utl.execute_query(con, qs.create_comments_table)


    # # 4. ВСТАВКА ЗАПИСЕЙ
    # users = [tuple(user) for user in data['users']]
    # user_records = ", ".join(["%s"] * len(users))
    # cursor = con.cursor()
    # cursor.execute(qs.insert_user_query(user_records), users)

    # posts = [tuple(post) for post in data['posts']]
    # post_records = ", ".join(["%s"] * len(posts))
    # cursor = con.cursor()
    # cursor.execute(qs.insert_post_query(post_records), posts)

    # utl.execute_query(con, qs.create_comments)

    # # Второй подход использует метод cursor.executemany(), который принимает два параметра:
    #     # 1. Строка query, содержащая заполнители для вставляемых записей.
    #     # 2. Список записей, которые мы хотим вставить.
    # val = [(4, 5), (3, 4)]
    # cursor = con.cursor()
    # cursor.executemany(qs.insert_likes_query, val)  
    # con.commit()


    # # 5. ИЗВЛЕЧЕНИЕ ДАННЫХ ИЗ ЗАПИСЕЙ
    # users = utl.execute_read_query(con, qs.select_users)
    # for user in users:
    #     print(user)

    # users_posts = utl.execute_read_query(con, qs.select_users_posts)
    # for users_post in users_posts:
    #     print(users_post)

    # # Следующий скрипт возвращает все сообщения вместе с комментариями к сообщениям и именами пользователей, которые разместили комментарии:
    # posts_comments_users = utl.execute_read_query(con, qs.select_posts_comments_users)
    # for posts_comments_user in posts_comments_users:
    #     print(posts_comments_user)

    # # Чтобы вернуть имена столбцов, нужно забрать атрибут description объекта cursor.
    # cursor = con.cursor()
    # cursor.execute(qs.select_posts_comments_users)
    # cursor.fetchall()
    # column_names = [description[0] for description in cursor.description]
    # print(column_names)


    # # 6. ОБНОВЛЕНИЕ ЗАПИСЕЙ ТАБЛИЦЫ
    # # В качестве примера обновим текст поста с id равным 2. Сначала создадим описание для SELECT:
    # post_description = utl.execute_read_query(con, qs.select_post_description)
    # for description in post_description:
    #     print(description)

    # # Следующий скрипт обновит описание:
    # utl.execute_query(con, qs.update_post_description)

    # # Теперь, если мы выполним SELECT-запрос еще раз, увидим следующий результат:
    # post_description = utl.execute_read_query(con, qs.select_post_description)
    # for description in post_description:
    #     print(description)


    # # 7. УДАЛЕНИЕ ЗАПИСЕЙ ТАБЛИЦЫ
    # utl.execute_query(con, qs.delete_comment)


    # # 8. ЗАКРЫВАЕМ КОНЭКШИН С БАЗОЙ И УДОЛЯЕМ КАСТОМНУЮ БАЗУ
    # utl.close_connection(con)
    # con = utl.create_connection(**data['defaul_db'])
    # utl.execute_query(con, qs.drop_database_query)
    # utl.close_connection(con)