import aiosqlite


async def create_db_or_connect_to_it():
    """Создаем БД или же подключаемся к ней."""

    conn = await aiosqlite.connect('articles.db')
    cur = await conn.cursor()

    # Создаем таблицу в БД или же если она создана подключаемся к ней.
    await cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        Имя_автора TEXT,
        Количество_лайков TEXT,
        Количество_комментариев TEXT,
        Количество_репостов TEXT,
        Название_статьи TEXT,
        Количество_просмотров_статьи TEXT,
        Тематика_статьи TEXT,
        Время_добавлений_статьи TEXT,
        Ссылка_на_автора_статьи TEXT,
        Ссылка_на_статью TEXT,
        Текст_статьи TEXT);
    """)

    # Сохраняем изменения.
    await conn.commit()

    print("Создали БД или же подключились к ней.")


async def clear_db():
    """Очищаем БД."""
    conn = await aiosqlite.connect('articles.db')
    cur = await conn.cursor()

    await cur.execute("""DELETE FROM articles""")
    await conn.commit()

    print("Очистили БД.")


async def add_data_to_db(tuple_with_data):
    """Добавляем данные в БД."""
    conn = await aiosqlite.connect('articles.db')
    cur = await conn.cursor()

    # Сохраняем данные в таблице articles.
    await cur.execute("""INSERT INTO articles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (tuple_with_data))
    await conn.commit()

    print("Добавили данные в БД.")