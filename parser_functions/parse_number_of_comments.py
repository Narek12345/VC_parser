def parse_number_of_comments(article_soup):
	"""Парсим количество комментариев."""
	try:
		number_article_comments = eval(article_soup.find('div', class_="l-hidden entry_data").get("data-article-info").replace("false", "False").replace("true", "True"))["comments"]
	except:
		number_article_comments = "Нет данных"

	return number_article_comments
