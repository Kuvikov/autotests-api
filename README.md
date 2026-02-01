# Autotests API
Проект автоматизации тестирования API с использованием современных инструментов и практик.

## Клонировать репозиторий
```bash
git clone https://github.com/Kuvikov/autotests-api.git
cd autotests-api
```

## Создать виртуальное окружение
```python
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
```
## или
```shell
venv\Scripts\activate     # Windows
```

## Установить зависимости
```python
pip install --upgrade pip
pip install -r requirements.txt
```

## Настроить переменные окружения
```bash
mcedit .env
```

## Отредактировать .env файл
```text
TEST_DATA.IMAGE_PNG_FILE="путь к файлу"

HTTP_CLIENT.URL="http://свой сервер"
HTTP_CLIENT.TIMEOUT=100
```