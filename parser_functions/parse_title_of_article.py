async def parse_title_of_article(article_soup):
	"""Парсим название статьи."""
	try:
		article_name = article_soup.find('h1', class_="content-title").text.strip().replace("\n\n\nСтатьи редакций", "")
	except:
		article_name = "Нет данных"

	return article_name