import sqlite3


class DB():
	"""Класс для работы с БД."""

	def __init__(self):

		# Создаем БД или же подключаемся к ней.
		self.conn = sqlite3.connect('articles.db')

		# Создаем обьект cursor.
		self.cur = self.conn.cursor()

		# Создаем таблицу в БД или же если она создана подключаемся к ней.
		self.cur.execute("""CREATE TABLE IF NOT EXISTS articles(
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
		self.conn.commit()


	def adding_data(self, data_tuple):
		"""Добавление данных в нашу таблицу articles."""
		
		# Сохраняем данные в таблице articles.
		self.cur.execute("""INSERT INTO articles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (data_tuple))

		# Сохраняем изменения.
		self.conn.commit()


	def clear_table(self):
		"""Очищаем нашу таблицу articles."""

		# Очищаем нащу табличку.
		self.cur.execute("""DELETE FROM articles""")

		# Сохраняем изменения.
		self.conn.commit()
