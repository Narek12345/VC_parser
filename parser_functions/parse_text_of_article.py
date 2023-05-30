async def parse_text_of_article(article_soup):
	"""Парсим текст статьи."""
	try:
		# Текст статьи.
		article_text = ""

		# Парсим текст статьи.
		texts = article_soup.find('div', class_="l-entry__content").find_all("p")

		for text in texts:
			text = text.text.strip()
			article_text += text

	except:
		article_text = "Нет данных"

	return article_text