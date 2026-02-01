## Server run

```shell
cd qa-automation-engineer-api-course/
uvicorn main:app --reload
```

```python
python -m pytest -v -s          # Где -s для вывода принтов, а -v для вывода подробной информации 
python -m pytest -k "login"     # Поиск тестов по совпадению слов
"""
Запуск всех тестов, где имя функции содержит "login" и "success":

python -m pytest -k "login and success"
"""
```

```text
- *Pydantic* отвечает за удобное преобразование данных.
- *jsonschema.validate* проверяет их корректность.
```