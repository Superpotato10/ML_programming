## Структура проекта
- `app/main.py` — FastAPI‑приложение с `/ping`
- `requirements_ML.txt`, `requirements_service.txt`, `requirements_jupyter.txt` — списки зависимостей по задачам
- `.venv/` — виртуальное окружение (не коммитим, защищено `.gitignore`)
- `image.png` — скриншоты команд

## Зачем использовать uv
[`uv`](https://github.com/astral-sh/uv) объединяет установку зависимостей и управление виртуальными окружениями. Он кэширует скачанные пакеты, использует параллельную загрузку и значительно ускоряет работу по сравнению с классическим `pip + python -m venv`.

## Установка uv
```powershell
pip install uv
```
Проверьте установку:
```powershell
uv --version
```

## Создание и активация виртуального окружения через uv
```powershell
# 1. Создать каталог проекта (если ещё нет)
mkdir ML_project
cd ML_project

# 2. Создать окружение .venv с помощью uv
uv venv .venv

# 3. Активировать окружение (PowerShell)
.\.venv\Scripts\Activate.ps1
```
После активации каждая команда в терминале имеет префикс `(.venv)`, что означает — все пакеты ставятся внутрь этого окружения.

## Установка зависимостей uv pip
`uv` предоставляет совместимую обёртку над `pip`, но использует собственный кэш.
```powershell
uv pip install -r requirements_ML.txt
uv pip install -r requirements_service.txt
uv pip install -r requirements_jupyter.txt
```
Повторные установки выполняются быстрее, потому что пакеты берутся из локального кеша.

## Проверка FastAPI-приложения
```powershell
uvicorn app.main:app --reload
```
- root (`/`) возвращает 307 Redirect → `/ping`
- `/ping` → `{"status":"ok"}`

## Финальные шаги и GitHub
```powershell
git init
git add .
git commit -m "Add FastAPI ping app"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```

## Отчёт
- Скриншоты последовательности команд — `image.png`.
- Трудности: браузер ожидал `/ping`, поэтому добавлен редирект с `/`.
- В результате проект полностью управляется через виртуальное окружение, созданное и обслуживаемое `uv`.
