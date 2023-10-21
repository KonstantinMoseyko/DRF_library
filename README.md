# Backend - Developer - Тестовое Задание

API библиотеки

Стек технологий:\
Django + Django ORM + DRF + Postgres

## Инструкция по сборке и запуску сервиса

  1. Клонируйте репозиторий
     ```sh
     git clone https://github.com/KonstantinMoseyko/DRF_library.git
     ```
  
  2. Установка и создание пакета виртуального окружения
     ```sh
     sudo apt install python3-virtualenv
     virtualenv -p python3 venv
     ```
  
  3. Активация виртуального окружения
     ```sh
     source venv/bin/activate
     ```

  4. Установка зависимостей
     ```sh
     pip install -r requirements.txt
     ```

  5. Далее применяем миграции, создаем тестовые данные кастомной командой \
     и запускаем тестовывй сервер
     ```sh
     python manage.py migrate
     python manage.py create_data
     python manage.py runserver
     ```
     Приложение будет доступно по адресу http://127.0.0.1:8000/api/ \
     Swagger - http://127.0.0.1:8000/swagger \
     GraphQL - http://127.0.0.1:8000/graphql

## Инструкция по запуску docker-compose
    
  1. Предполагается, что у пользователя уже установлены docker и docker-compose.\
     Запускаем контейнеры
     ```sh
     docker compose up --build
     ```
  
  2. После запуска проекта вам нужно находиться в корневой директори проекта,\
     создадим тестовые данные
     ```sh
     docker exec drf_library-backend-1 python manage.py create_data
     ```
     Приложение будет доступно по адресу http://0.0.0.0:8080/api/