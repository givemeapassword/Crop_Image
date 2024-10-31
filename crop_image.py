#сервис по редактированию пачек изображений
#берет с папки изображения и резит их на нужный размер
#и переводит в PNG

from PIL import Image
import os

def give_me_a_data():

    format_expansion_list = {1:"png",
                             2:"jpg"}
    
    path = input("Введите путь до архива с фотографиями: " )
    path = os.path.abspath(path)
    if not os.path.exists(path):
        print("Такой папки не существует")
        print("Прощайте!")
        return
    
    format_crop = int(input("Выберете формат обрезания((1) \"512x512\" (2) \"256x256): "))
    if format_crop != (1 or 2):
        print("Напишите правильно формат данных!")
        print("Прощайте!")
        return

    format_expansion =  int(input("Выберете формат расширения((1) \"png\" (2) \"jpg\"): "))
    if format_expansion != (1 or 2):
        print("Напишите правильно формат данных!")
        print("Прощайте!")
        return
    format_expansion = format_expansion_list[format_expansion]


    path = os.path.abspath(path) #перевод пути в абсолютный
    path_dir = create_folder(path)
    crop_image(path,path_dir,format_crop,format_expansion)
    
def crop_image(path_image,path_dir,format_crop,format_expansion):
    files = os.listdir(path_image)
    left_top  = {1:[0,100,512,512],
                 2:[50,50,256,256]}
    for file in files:
        try:
            if os.path.isdir(os.path.join(path_image,file)):
                continue
            image = Image.open(os.path.join(path_image,file))
        except IOError:
            print(f"Не смог открыть файл: {os.path.join(path_image,file)}")
            continue
        print(f"Обрезка фото: {os.path.join(path_image,file)}")
        print(f"Перевод файла в формат: {format_expansion}")
        cropped = image.crop(tuple(left_top[format_crop]))
        file_name, _ = os.path.splitext(file)
        new_file_name = f"{file_name}.{format_expansion.lower()}"
        cropped.save(os.path.join(path_dir, new_file_name), format_expansion)
             
def create_folder(path):
    path_folder = os.path.join(path,"ImageFolder")
    print(f"Папка с фотографиями: {path_folder}")
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
        print(f"Создана папка по пути: {path_folder}")
    return path_folder
        
    
if __name__ == "__main__":
    give_me_a_data()
    end = input("Введите любую кнопку...")