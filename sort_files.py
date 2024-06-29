import os

def full_path(file_name):
    current_directory = os.getcwd()
    folder = 'sorted'
    full_path = os.path.join(current_directory, folder, file_name)
    return full_path


def open_file(file_name):
    with open(full_path(file_name), "r", encoding="utf8") as file:
        content = file.readlines()
        return content

def sort_content(files_list):
    len_list = []
    for doc in files_list:
        len_list.append(len(open_file(doc)))
    len_list_2 = len_list.copy()
    while len(len_list) != 0:
        min_index = len_list_2.index(min(len_list))
        with open('sorted_files.txt', "a") as file:
            file.write(f"{files_list[min_index]}\n")
            file.write(f"{min(len_list)}\n")
            content = open_file(files_list[min_index])
            for line in content:
                file.write(line)
            if not content[-1].endswith('\n'):
                file.write('\n')
            len_list.remove((min(len_list)))
            
sort_content(["1.txt", "2.txt", "3.txt"])