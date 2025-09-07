import os
print(f"Имя ОС: {os.name}")
print(os.getcwd())

directory_path = "."


if not os.path.exists(directory_path):
    print(f"Директория {directory_path} не существует!")
    exit()


files = []
for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        files.append(item)

print(f"Найдено {len(files)} файлов для сортировки...")


folder_info = {}


for filename in files:

    name, extension = os.path.splitext(filename)
    extension = extension.lower() or '.no_extension'


    folder_name = extension[1:] if extension != '.no_extension' else 'no_extension'


    source_path = os.path.join(directory_path, filename)
    folder_path = os.path.join(directory_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    destination_path = os.path.join(folder_path, filename)
    os.rename(source_path, destination_path)


    file_size = os.path.getsize(destination_path)
    if folder_name not in folder_info:
        folder_info[folder_name] = {'count': 0, 'size': 0}

    folder_info[folder_name]['count'] += 1
    folder_info[folder_name]['size'] += file_size



for folder_name, info in folder_info.items():
    size_gb = info['size'] / (1024 ** 3)  # Конвертируем в гигабайты
    print(f"В папке '{folder_name}' перемещено {info['count']} файлов, "
          f"их суммарный размер - {size_gb:.2f} гигабайт")


for folder_name in folder_info:
    folder_path = os.path.join(directory_path, folder_name)

    try:
        folder_files = [f for f in os.listdir(folder_path)
                        if os.path.isfile(os.path.join(folder_path, f))]

        if folder_files:
            old_name = folder_files[0]
            name, ext = os.path.splitext(old_name)
            new_name = f"renamed_{name}{ext}"

            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)


            os.rename(old_path, new_path)
            print(f"\nФайл {old_name} был переименован в {new_name}")
            break

    except Exception as e:
        print(f"Ошибка при переименовании файла в папке '{folder_name}': {e}")