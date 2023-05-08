def parse_number_of_article_views(article_soup):
	"""Парсим количество просмотров статьи."""
	try:
		number_article_views = article_soup.find('span', class_="views__value").text.strip()
	except:
		number_article_views = "Нет данных"

	return number_article_views