# Crop Photos Script

Этот скрипт предназначен для обрезки изображений из заданной папки и сохранения их в другую папку. Скрипт поддерживает форматы файлов JPG и PNG, а также позволяет задавать размеры обрезки - 512x512 или 256x256 пикселей. Для работы используется библиотека Pillow.

## Установка

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше).
2. Установите библиотеку Pillow с помощью pip:

   `pip install Pillow`

## Создание EXE файла

Чтобы создать исполняемый файл (EXE) из скрипта, выполните следующие шаги:

1. Установите библиотеку pyinstaller:

   `pip install pyinstaller`
   
2. В командной строке перейдите в директорию с вашим скриптом и выполните команду:

   `pyinstaller --onefile crop_photos.py`
   
3. После завершения процесса, EXE файл можно будет найти в папке dist.  
