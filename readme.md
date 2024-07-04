# 📧 Сервис Подтверждения Email на FastAPI

Добро пожаловать в **Сервис Подтверждения Email на FastAPI**! Это приложение предназначено для управления подтверждением адресов электронной почты пользователей через отправку писем с уникальными токенами. Используя FastAPI и SQLAlchemy, приложение обеспечивает удобную и быструю интеграцию механизма подтверждения email в ваш проект.

## 🎯 Возможности

- **Отправка подтверждающего email**: Создание нового пользователя или повторная отправка подтверждающего письма для уже существующего.
- **Подтверждение email**: Подтверждение email пользователя по уникальному токену.
- **Обработка ошибок**: Удобная обработка ошибок и исключений, связанных с неверными или просроченными токенами.
- **Миграции базы данных**: Управление схемой базы данных с помощью Alembic.

## 🚀 Начало работы

### Предварительные требования

Убедитесь, что у вас установлено следующее:

- Python 3.8+
- Docker и Docker Compose

### Установка

1. **Клонируйте репозиторий:**
    ```sh
    git clone https://github.com/artyoma2000/fastapi-email-confirmation.git
    cd fastapi-email-confirmation
    ```

2. **Создайте файл `.env` на основе `.env.example` и заполните его нужными параметрами:**
    ```sh
    cp .env.example .env
    ```

3. **Запустите Docker Compose:**
    ```sh
    docker-compose up -d
    ```

4. **Примеры JSON-запросов:**
Для проверки работы сервиса подтверждения email на FastAPI вам потребуется отправить несколько типов JSON-запросов: для отправки подтверждающего email и для подтверждения email через токен.

### Примеры JSON-запросов

#### Отправка подтверждающего email

**Запрос**:
```http
POST /send-confirmation/
```

**Пример JSON**:
```json
{
    "email": "user@example.com"
}
```

**Curl**:
```sh
curl -X POST "http://localhost:8000/send-confirmation/" -H "Content-Type: application/json" -d '{"email": "user@example.com"}'
```

**Пример ответа**:
```json
{
    "message": "Confirmation email sent successfully"
}
```
или
```json
{
    "message": "Email is already confirmed"
}
```

#### Подтверждение email через токен

**Запрос**:
```http
GET /confirm-email/?token=<token>
```

**Пример URL**:
```plaintext
http://localhost:8000/confirm-email/?token=your_confirmation_token
```

**Curl**:
```sh
curl -X GET "http://localhost:8000/confirm-email/?token=your_confirmation_token"
```

**Пример ответа**:
```json
{
    "message": "Email confirmed successfully"
}
```
или
```json
{
    "detail": "Invalid or expired token"
}
```

### Структура проекта

```plaintext

main.py                # Основной файл приложения
config.py              # Конфигурационные параметры
database.py            # Инициализация базы данных
email_service.py       # Функции для отправки email
models.py              # Описание моделей базы данных
requirements.txt       # Зависимости Python
Dockerfile             # Dockerfile для создания образа приложения
docker-compose.yml     # Docker Compose файл для запуска сервисов
.env                   # Пример файла окружения
```

### Конфигурация

- **SMTP сервер**: Настройки SMTP сервера для отправки подтверждающих писем.
- **DATABASE_URL**: URL для подключения к базе данных PostgreSQL.
- **SECRET_KEY**: Секретный ключ для приложения.

## 🛠️ Разработка

### Полезные команды

- **Запуск приложения в режиме разработки:**
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

- **Создание новой миграции:**
    ```sh
    alembic revision --autogenerate -m "Описание миграции"
    ```

- **Применение миграций:**
    ```sh
    alembic upgrade head
    ```

### Будущие улучшения

- **Аутентификация пользователей**: Добавление функции регистрации и аутентификации пользователей.
- **Логирование**: Внедрение системы логирования для улучшенного мониторинга и отладки.
- **Интернационализация**: Добавление поддержки нескольких языков.

## 🤝 Участие

Мы приветствуем вклад в улучшение этого проекта. Пожалуйста, следуйте стандартному рабочему процессу fork-branch-pull request:

1. Сделайте форк репозитория
2. Создайте новую ветку (`git checkout -b feature/your-feature`)
3. Закоммитьте ваши изменения (`git commit -am 'Добавить новую функцию'`)
4. Отправьте изменения в ветку (`git push origin feature/your-feature`)
5. Создайте новый Pull Request

## 📜 Лицензия

Этот проект лицензирован под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

