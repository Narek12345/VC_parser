async def parse_number_of_likes(article_soup):
	"""Парсим количество лайков."""
	try:
		number_article_likes = eval(article_soup.find('div', class_="l-hidden entry_data").get("data-article-info").replace("false", "False").replace("true", "True"))["likes"]
	except:
		number_article_likes = "Нет данных"
			
	return number_article_likes