from psycopg2 import connect, OperationalError


# Определим функцию create_connection() для подключения к базе данных PostgreSQL:
def create_connection(**db_data):
    connection = None
    try:
        db_name = db_data['db_name']
        # Подключение осуществляется через интерфейс psycopg2.connect()
        connection = connect(
            database=db_name,
            user=db_data['db_user'],
            host=db_data['db_host'],
            port=db_data['db_port'],
        )
        # autocommit = True гарантирует, что psycopg выполнит каждый оператор и немедленно зафиксирует его.
        connection.autocommit = True
        print(f"Connection to PostgreSQL DB {db_name} successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
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