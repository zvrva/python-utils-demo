# python-utils-demo

Небольшой pet-проект с утилитами на Python. В проекте специально оставлены баги,
которые выявляются тестами. Репозиторий предназначен как "жертва" для демонстрации
работы внешнего SDLC-агента

## Требования
- Python 3.11+

## Как запустить тесты локально

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements-dev.txt
pytest -q # Или:  python -m pytest -q```

Примечание: на текущем состоянии репозитория тесты падают, т.к. в коде есть ошибки,
которые нужно исправить

