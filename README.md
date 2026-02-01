# Autotests API
Проект автоматизации тестирования API с использованием современных инструментов и практик.
### Технологический стек
```
pytest, httpx, pydantic, allure, Faker, jsonschema
```
# Быстрый старт
### Технологический стек
```
pytest, httpx, pydantic, allure, Faker, jsonschema, 
```
# Быстрый старт
### Технологический стек
```
pytest, httpx, pydantic, allure, Faker, jsonschema, 
```
# Быстрый старт
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

## Настройка рабочего пространства VS Code
### Форматирование и линтинг:
- Black Formatter: форматирование Python кода
    - Длина строки: 99 символов
    - Без нормализации строк
    - Preview режим (новые возможности)

- Flake8: линтинг Python кода
    - Длина строки: 99 символов
    - Игнорируется правило E203 (пробелы перед :)

- Isort: сортировка импортов
    - Автоматическая организация импортов при сохранении

- Автоматизация:
    - "editor.formatOnSave": true - автоформатирование при сохранении
    - "editor.codeActionsOnSave": { "source.organizeImports": "explicit" } - автосортировка импортов
    - Используется Python 3.11 из виртуального окружения venv

- Тестирование:
    - Используется pytest (unittest отключен)
    - Аргументы pytest: ["."] (текущая директория)
    - Автодетект тестов pytest

- Исключения файлов:
    - Скрыты временные файлы Python (__pycache__, .pytest_cache)
    - Скрыты build-артефакты и egg-info файлы

### Использовать можно через VS Code
```
В левом верхнем углу "File" → Open Workspace... → выбрать vscode.code-workspace
```

## Описание проекта
