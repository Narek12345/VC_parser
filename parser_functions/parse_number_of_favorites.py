def parse_number_of_favorites(article_soup):
	"""Парсим количество сделанных репостов."""
	try:
		# Парсим html блок div с данными.
		number_favorites = eval(article_soup.find('div', class_="l-hidden entry_data").get("data-article-info").replace("false", "False").replace("true", "True"))["favorites"]
	except:
		number_favorites = "Нет данных"

	return number_favorites