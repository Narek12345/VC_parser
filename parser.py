from bs4 import BeautifulSoup
from selenium import webdriver

import requests

import db
import parser_functions as func


# Создаем экземпляр БД.
db = db.DB()


# Просим пользователя ввести количество статей, которые надо спарсить.
while True:
	try:
		number_of_articles_to_parse = int(input("Введите количество статей, которые надо спарсить: "))
		break
	except:
		print("\nВводите только целочисленные значения.")
		continue


# Открываем Chrome.
driver = webdriver.Chrome()
# Открываем сайт vc.ru.
driver.get("https://vc.ru/popular")

# Сохраняем весь контент в этой переменной.
html = driver.page_source
# Фильтруем весь контент и оставляем только html.
soup = BeautifulSoup(html, 'lxml')


# Получаем ссылки на все появившиеся статьи.
article_links = soup.find_all('a', class_="content-link", attrs={"data-analytics": "Popular — Feed Item"})

# Проверяем длину статей с длиной вводимым от пользователя.
if len(article_links) < number_of_articles_to_parse:
	while True:
		# Сравниваем оба значения.
		if len(article_links) < number_of_articles_to_parse:
			# Листаем сайт.
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Присоединяем к нашему списку данных еще и новые данные.
			article_links.extend(soup.find_all('a', class_="content-link", attrs={"data-analytics": "Popular — Feed Item"}))
		else:
			break

# Создаем нужный срез который выбрал пользователь.
article_links = article_links[:number_of_articles_to_parse]


# Перед добавлением данных в таблицу articles уу сначало надо очистить.
db.clear_table()



for link in article_links:

	# Берем ссылку на статью.
	article_url = link.get("href")
	# Переходим по ссылке.
	req = requests.get(article_url)
	# Фильтруем весь контент и оставляем только html.
	article_soup = BeautifulSoup(req.text, 'lxml')

	# Парсим имя автора.
	author_name = func.parse_name_of_author.parse_name_of_author(article_soup)

	# Парсим количество лайков.
	number_article_likes = func.parse_number_of_likes.parse_number_of_likes(article_soup)

	# Парсим количество комментариев.
	number_article_comments = func.parse_number_of_comments.parse_number_of_comments(article_soup)

	# Парсим количество репостов.
	number_article_favorites = func.parse_number_of_favorites.parse_number_of_favorites(article_soup)

	# Парсим название статьи.
	article_name = func.parse_title_of_article.parse_title_of_article(article_soup)

	# Парсим количество просмотров статьи.
	number_article_views = func.parse_number_of_article_views.parse_number_of_article_views(article_soup)

	# Парсим тематику статьи.
	article_topic = func.parse_topic_of_article.parse_topic_of_article(article_soup)

	# Парсим время добавлений статьи.
	article_publish_time = func.parse_time_of_adding_article.parse_time_of_adding_article(article_soup)

	# Парсим ссылку на автора статьи.
	author_link = func.parse_link_to_author_of_article.parse_link_to_author_of_article(article_soup)

	# Парсим текст статьи.
	article_text = func.parse_text_of_article.parse_text_of_article(article_soup)


	data_tuple = (author_name, number_article_likes, number_article_comments, number_article_favorites, article_name, number_article_views, article_topic, article_publish_time, author_link, article_url, article_text)


	# Добавляем данные в БД.
	db.adding_data(data_tuple)