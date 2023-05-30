async def parse_link_to_author_of_article(article_soup):
	"""Парсим ссылку на автора статьи."""
	try:
		# Парсим ссылку на автора статьи.
		author_link = article_soup.find('a', class_="content-header-author__name").get("href")
	except:
		author_link = "Нет данных"

	return author_link