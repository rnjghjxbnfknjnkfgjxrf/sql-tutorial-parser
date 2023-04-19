# sql-tutorial-parser
Парсер, получающий все упражнения и их решения с сайта [sql-tutorila](http://www.sql-tutorial.ru/ru).
По умолчанию полученная информация записывается в файл `result.json`
## Установка
### MS Windows
```
python -m venv <venv_name>
.\<venv_name>\Scripts\Activate.ps1
pip install -r requirements.txt
```
### Linux
```
python3 -m venv <venv_name>
source <venv_name>/bin/activate
pip install -r requirements.txt
```

## Использование
```
python3 main.py
```
