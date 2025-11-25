# ML_programming

# 1. Создаем папку проекта
mkdir venv_lab
cd venv_lab

<img width="225" height="103" alt="image" src="https://github.com/user-attachments/assets/fd79d720-d489-4893-9086-9b6c5fc8d728" />


# 2. Создаем виртуальное окружение
python -m venv .venv

<img width="221" height="181" alt="image" src="https://github.com/user-attachments/assets/ba6e9cd1-1850-41c7-aee9-bee29ff5d4e0" />


# 3. Активируем venv (PowerShell)
.\.venv\Scripts\Activate.ps1

# Должно появиться (.venv) в начале строки
<div align="center">
  <img width="433" height="48" alt="image" src="https://github.com/user-attachments/assets/a86c198e-d112-4ed8-a2c6-3a7830479d26" />
</div>

# 4. Создаём необходимые документы
<div align="center">
  <img width="207" height="73" alt="image" src="https://github.com/user-attachments/assets/5509a3be-9579-4373-9f59-9f854a8d2fed" / alt="Список необходимых документов">
</div>

### В каждом из документов перечислены необходимые версии библиотек, которые надо установить для работы с проектом:
### Содержание файла requirements_jupyter.txt:

<div align="center">
  <img width="536" height="962" alt="image" src="https://github.com/user-attachments/assets/cf02098e-d261-48a6-898e-e7c7320b33f6" / alt="Содержание файла requirements_jupyter.txt" >
</div>

<div align="center">
  <img width="1245" height="960" alt="image" src="https://github.com/user-attachments/assets/fb33db0f-f519-4c7a-a25f-502ca4867fa1" / alt="Содержание файла requirements_jupyter.txt">
</div>

<div align="center">
  <img width="1143" height="986" alt="image" src="https://github.com/user-attachments/assets/70b85297-4384-4761-90ea-4db81f6fe673" / alt="Содержание файла requirements_jupyter.txt">
</div>

### Содержание файла requirements_ML.txt:

<div align="center">
  <img width="321" height="432" alt="image" src="https://github.com/user-attachments/assets/6f25d29c-b8e0-4d1d-8f8d-983c06705b2e" / alt="Содержание файла requirements_ML.txt" >
</div>

### Содержание файла requirements_service.txt:
<div align="center">
  <img width="798" height="959" alt="image" src="https://github.com/user-attachments/assets/cfa77de9-f26c-43f4-b200-113005dad1ee" / alt="Содержание файла requirements_service.txt" >
</div>
<div align="center">
  <img width="595" height="926" alt="image" src="https://github.com/user-attachments/assets/5033a2b8-7466-4cb8-ac9a-474980efcffa" / alt="Содержание файла requirements_service.txt">
</div>

# 5. Сделаем простое FastAPI-приложение app/main.py с эндпоинтом':
# GET /ping → {"status":"ok"}

<div align="center">
  <img width="422" height="329" alt="image" src="https://github.com/user-attachments/assets/ba5b9b16-f88b-467f-bc30-d3a233c6812c" / alt="Код для создания простого FastAPI-приложения app/main.py с эндпоинтом">
</div>



