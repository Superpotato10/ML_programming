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
<div align="center">
<img width="557" height="122" alt="image" src="https://github.com/user-attachments/assets/400fcaec-6f71-422d-9a8a-1e00babb5b9b" />
</div>

Проверьте установку:
```powershell
uv --version
```

<div align="center">
<img width="460" height="34" alt="image" src="https://github.com/user-attachments/assets/88b5b876-71ee-4797-83f0-a6efe911d4f2" />
</div>

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
Ниже на скриншотах представлен процесс установки необходимых пакетов.

<div align=center>
<img width="919" height="425" alt="image" src="https://github.com/user-attachments/assets/bb097d26-7b9e-4f83-a962-5cf09497f99f" />
<img width="750" height="276" alt="image" src="https://github.com/user-attachments/assets/0051601a-351b-4751-a696-7740f5ccb56c" />
<img width="730" height="129" alt="image" src="https://github.com/user-attachments/assets/fe01fa0e-bd88-49f0-a0ef-c4ce5fe0f3b1" />
</div>

## Проверка FastAPI-приложения
```powershell
uvicorn app.main:app --reload
```
- root (`/`) возвращает 307 Redirect → `/ping`
- `/ping` → `{"status":"ok"}`


