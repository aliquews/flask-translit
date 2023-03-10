# Flask translit service

Данный сервис реализует функционал транслитерации текста с русского на английский. Также он способен формировать отчеты на главной странице и выдавать xlsx файл со всеми транслитами пользователю.

# Архитектура проекта
```
root
│   README.md
│   alembic.ini    
│
└───migrations
│   └───versions # папка с миграциями
│   │   env.py # конфигурация alembic
│
│   
└───src
    └───files # тут хранятся файлы exel
    └───db
    │   │   database.py # база данных и сессии
    │   │   db_operations.py # операции с дб (в данном случае добавление)
    │   │   models.py # модели pydantic
    │   │   tables.py # таблицы в бд 
    │
    └───logic
    │   │   export_data.py # экспорт данных из дб в exel 
    │   │   get_data.py
    │
    └───templates
    │   │   index.html
    │
    │   main.py
```
# Скриншоты 
[![Screenshot-from-2023-02-18-17-14-46.png](https://i.postimg.cc/wjTqcCQR/Screenshot-from-2023-02-18-17-14-46.png)](https://postimg.cc/N5SvQPVQ)

[![Screenshot-from-2023-02-18-17-17-57.png](https://i.postimg.cc/BZMwPRbV/Screenshot-from-2023-02-18-17-17-57.png)](https://postimg.cc/14VKLCpG)

[![Screenshot-from-2023-02-18-17-18-52.png](https://i.postimg.cc/kG4syXGh/Screenshot-from-2023-02-18-17-18-52.png)](https://postimg.cc/2bsnkY44)

[![Screenshot-from-2023-02-18-17-20-03.png](https://i.postimg.cc/kG684VB9/Screenshot-from-2023-02-18-17-20-03.png)](https://postimg.cc/jnTC3SHk)

## Установка
### Клонирование репозитория
`git clone https://github.com/aliquews/flask-translit.git`
### Запуск через docker compose
`docker-compose up --build -d`

#### На этом установка завершена, можно использовать [сервис](http://localhost:5000/).
