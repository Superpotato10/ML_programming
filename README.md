# ML_programming

# 1. Создаем папку проекта
mkdir venv_lab
cd venv_lab
<div align="center">
  <img width="225" height="103" alt="image" src="https://github.com/user-attachments/assets/fd79d720-d489-4893-9086-9b6c5fc8d728" />
 </div>

# 2. Создаем виртуальное окружение
python -m venv .venv
<div align="center">
  <img width="221" height="181" alt="image" src="https://github.com/user-attachments/assets/ba6e9cd1-1850-41c7-aee9-bee29ff5d4e0" />
</div>

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

# Установка файлов с необходимыми требованиями

Для установки requirements-файлов используется стандартная команда 
### pip install -r (название файла).txt

Ниже показан пример установки файлов.

### Установка файла requirements_ML.txt
Для установки библиотек, перечисленных в файле, вам необходимо запустить следующую команду:
### pip install -r requirements_ML.txt   
<div align="center">
  <img width="1131" height="592" alt="image" src="https://github.com/user-attachments/assets/7f140f8c-74f5-4d3a-a6d8-e8fde7237018" />
</div>

Розовым цветом и стрелочками на изображении отмечены:
- команда, которую необходимо ввести для установки файла;
- сообщение об успешной установке библиотек, перечисленных в файле.

### Файлы requirements_service.txt и requirements_jupyter.txt устанавливаются аналогичным образом.

# 5. Сделаем простое FastAPI-приложение app/main.py с эндпоинтом':
# GET /ping → {"status":"ok"}

<div align="center">
  <img width="422" height="329" alt="image" src="https://github.com/user-attachments/assets/ba5b9b16-f88b-467f-bc30-d3a233c6812c" / alt="Код для создания простого FastAPI-приложения app/main.py с эндпоинтом">
</div>

# Запуск приложения
Для запуска приложения в командную строку необходимо ввести: 
**_uvicorn app.main:app --reload_ **
Приложение запустится.

### Пример работы приложения 
<div align="center">
  <img width="910" height="215" alt="image" src="https://github.com/user-attachments/assets/d614990b-3de8-4d81-b9e1-11c86a0493ec" />
  <img width="1071" height="126" alt="image" src="https://github.com/user-attachments/assets/ad9012c2-3798-4ea8-b76a-62ea4008609b" />
</div>

### Пример работы приложения (ошибка)
<div align="center">
  <img width="929" height="121" alt="image" src="https://github.com/user-attachments/assets/ab5730bb-7d6d-4b5b-ae40-c18140db1a8b" />
</div>


