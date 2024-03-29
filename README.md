# api_final
## API для учебного проекта yatube Яндекс Практикум


api_final это проект для взаимодействия с помощью архитектуры REST API с сайтом yatube

## Features

- Получение публикации
- Создание публикации
- Обновление публикации
- Частичное обновление публикации
- Удаление публикации
- Получение комментариев
- Добавление комментария
- Обновление комментария
- Частичное обновление комментария
- Удаление комментария
- Список сообществ
- Информация о сообществе
- Подписки
- Подписка
- Получить JWT-токен
- Обновить JWT-токен
- Проверить JWT-токен

## Installation
####  Для запуска потребуется:

##### Python: 3.9+
##### Виртуальное окружение:

###### Виртуальное окружение (установка модуля):
- на Linux(Ubuntu):
     > sudo apt install python3-venv
- на windows и MacOS
     > Для Windows и MacOS модуль venv доступен из коробки.

###### Виртуальное окружение (создание):
- на Unix системах
     > python3 -m venv имя_окружения
- на windows
     > python -m venv имя_окружения

###### Виртуальное окружение (активация):
- на Unix системах
     > source имя_окружения/bin/activate
- на windows
     > имя_окружения/scripts/activate.bat

##### Установка зависимостей:
- на Unix системах
     > python -m pip install -r requirements.txt
- на windows
     > py -m pip install -r requirements.txt

### Список библиотек (requirements.txt)
```sh
Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
djoser==2.1.0
```

## Примеры запросов
![Получение токена](blob:https://app.pachca.com/50c5a786-b2c7-497b-80c6-b7edfe5888c6)
![Получение публикаций](https://app.pachca.com/13b886a2-4b42-486f-bf09-605af9bebf13)
![Создание публикации](blob:https://app.pachca.com/2844f741-47ba-47a8-a664-7ed2c1889320)

** By Shelepov Nikita **