def parse_name_of_author(article_soup):
	"""Парсим имя автора."""
	try:
		author_name = eval(article_soup.find('div', class_="l-hidden entry_data").get("data-article-info").replace("false", "False").replace("true", "True"))["author_name"]
	except:
		author_name = "Нет данных"

	return author_name