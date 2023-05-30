from bs4 import BeautifulSoup
from selenium import webdriver

import requests, asyncio, time

import db
import parser_functions as func

start = time.time()


async def create_db_or_connect_to_it():
    """Создаем БД или подключаемся к ней."""
    await db.create_db_or_connect_to_it()


async def clear_db():
    """Очищаем БД."""
    await db.clear_db()


async def add_data_to_db(tuple_with_data):
    """Добавляем данные в БД."""
    await db.add_data_to_db(tuple_with_data)


async def parsing_an_article(article_soup, article_url):
    """Парсим статью."""

    # Парсим имя автора.
    author_name = await func.parse_name_of_author.parse_name_of_author(
        article_soup)

    # Парсим количество лайков.
    number_article_likes = await func.parse_number_of_likes.parse_number_of_likes(
        article_soup)

    # Парсим количество комментариев.
    number_article_comments = await func.parse_number_of_comments.parse_number_of_comments(
        article_soup)

    # Парсим количество репостов.
    number_article_favorites = await func.parse_number_of_favorites.parse_number_of_favorites(
        article_soup)

    # Парсим название статьи.
    article_name = await func.parse_title_of_article.parse_title_of_article(
        article_soup)

    # Парсим количество просмотров статьи.
    number_article_views = await func.parse_number_of_article_views.parse_number_of_article_views(
        article_soup)

    # Парсим тематику статьи.
    article_topic = await func.parse_topic_of_article.parse_topic_of_article(
        article_soup)

    # Парсим время добавлений статьи.
    article_publish_time = await func.parse_time_of_adding_article.parse_time_of_adding_article(
        article_soup)

    # Парсим ссылку на автора статьи.
    author_link = await func.parse_link_to_author_of_article.parse_link_to_author_of_article(
        article_soup)

    # Парсим текст статьи.
    article_text = await func.parse_text_of_article.parse_text_of_article(
        article_soup)

    data_tuple = (author_name, number_article_likes, number_article_comments,
                  number_article_favorites, article_name, number_article_views,
                  article_topic, article_publish_time, author_link,
                  article_url, article_text)

    await add_data_to_db(data_tuple)


async def open_chrome_and_get_all_links_to_articles():
    """Открываем хром и парсим ссылки на статьи."""

    # Открываем Chrome.
    driver = webdriver.Chrome()
    # Открываем сайт vc.ru.
    driver.get("https://vc.ru/popular")

    # Сохраняем весь контент в этой переменной.
    html = driver.page_source
    # Фильтруем весь контент и оставляем только html.
    soup = BeautifulSoup(html, 'lxml')

    # Получаем ссылки на все появившиеся статьи.
    article_links = soup.find_all(
        'a',
        class_="content-link",
        attrs={"data-analytics": "Popular — Feed Item"})

    # Просим пользователя ввести количество статей которые надо спарсить.
    while True:
        try:
            number_of_articles_to_parse = int(
                input("Введите количество статей, которые надо спарсить: "))
            break
        except:
            print("\nВводите только целочисленные значения.")
            continue

    # Проверяем длину статей с длиной вводимым от пользователя.
    if len(article_links) < number_of_articles_to_parse:
        while True:
            # Сравниваем оба значения.
            if len(article_links) < number_of_articles_to_parse:
                # Листаем сайт.
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")

                # Присоединяем к нашему списку данных еще и новые данные.
                article_links.extend(
                    soup.find_all(
                        'a',
                        class_="content-link",
                        attrs={"data-analytics": "Popular — Feed Item"}))
            else:
                break

    # Создаем нужный срез, который выбрал пользователь.
    article_links = article_links[:number_of_articles_to_parse]

    # Итерируемся по списку с ссылками на статьи.
    for link in article_links:
        # Берем ссылку на статью.
        article_url = link.get('href')
        # Переходим по ссылке.
        req = requests.get(article_url)
        # Фильтруем весь контент и оставляем только html.
        article_soup = BeautifulSoup(req.text, 'lxml')

        await parsing_an_article(article_soup, article_url)


async def main():
    async with asyncio.TaskGroup() as tg:
        # Подключаемся к БД.
        tg.create_task(create_db_or_connect_to_it())
        # Очищаем БД.
        tg.create_task(clear_db())
        # Открываем Chrome.
        tg.create_task(open_chrome_and_get_all_links_to_articles())


asyncio.run(main())

print("Конец!")

end = time.time()
print(f"Seconds: {end-start}")