Домашнє завдання #13

Друга частина

У цьому домашньому завданні був доопрацьований застосунок Django із домашнього завдання 10 згідно вимог:

Реалізуйте механізм скидання паролю для зареєстрованого користувача;
Усі змінні середовища повинні зберігатися у файлі .env та використовуватися у файлі settings.py;

Для роботи проекта необхідний файл `/hw10_django/.env` зі змінними оточення.
Створіть його з таким вмістом і підставте свої значення (Дивись також '/hw10_django/.env_example' ).

```dotenv
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Запуск баз даних

```bash
docker-compose up -d
```

Запуск застосунку

```
cd hw10_django
py manage.py runserver
```
