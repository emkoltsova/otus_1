# Устанавливаю базовый образ
FROM python:3.10-alpine

# Устанавливаю рабочий директорий внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /opencart_tests

# Копирую сначала зависимости
# Для того чтобы не пересобирать их каждый раз при сборке
COPY requirements.txt .

# Выполняю необходимые команды
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирую остальные файлы проекта
COPY . .

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
CMD ["pytest", "--browser", "chrome", "--executor","selenoid"]

# Создание образа
# docker build -t tests .
# Запуск контейнера с тестами
# docker run --name tests_run --network selenoid tests \
# && docker cp tests_run:/opencart_tests/allure-results . \
# && allure serve allure-results