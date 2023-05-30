async def parse_time_of_adding_article(article_soup):
	"""Парсим время добавления статьи."""
	try:
		# Парсим время добавления статьи.
		article_publish_time = article_soup.find('time', class_="time", attrs={"air-module": "module.date"}).get("title")
	except:
		try:
			article_publish_time = eval(article_soup.find('div', class_="l-hidden entry_data").get("data-article-info").replace("false", "False").replace("true", "True"))["date"]
		except:
			article_publish_time = "Нет данных"

	return article_publish_time