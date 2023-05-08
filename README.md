# VC parser

## Описание
Программа, которая собирает данные с сайта **vc.ru** из каталога **popular** и сохраняет эти данные в БД. При запуске этой программы вы можете сами выбрать количество блогов, которые вам надо чтобы программа спарсила.

## Как запустить
1. Первым дело вам надо будет клонировать репозиторий с кодом. Делается это довольно просто (_у вас должен быть установлен Git_):
  ```
  git clone https://github.com/Narek12345/VC_parser.git>
  ```
2. После клонирования вместе с репозиторием идет такой файлик, как requirements.txt. Он является довольно важным файлом, так как там указаны все зависимости проекта, которые надо будет установить. Переходим в консоли туда, где у нас requirements и пишем следующий код:
  ```
  pip install -r requirements.txt
  ```
3. После всех действий, совершенных в пунктах 1 и 2, вы можете со спокойной душой запустить parser.py в консоли (вы должны находиться в консоли там, где этот файл) и на этом о запуске проекта заканчивается.

## БД
В качестве БД я решил использовать простую, такую как SQLite3. В нем нету сложных функций, типов данных и т.д., но нам этого как раз и не надо. После запуска проекта у вас появится файл articles.db, который вы сможете открыть с помошью программы SQLite3.

## Способы связаться с автором
Если у вас возникают какие-то вопросы, то пишите мне в:  
***
**WhatsApp: +79887001838**
***
**Telegram: https://t.me/Narek_76**