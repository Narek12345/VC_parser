def parse_topic_of_article(article_soup):
	"""Парсим тему статьи."""
	try:
		# Парсим html блок div с данными.
		article_topic = article_soup.find('div', class_="content-header-author__name").text.strip()
	except:
		article_topic = "Нет данных"

	return article_topic