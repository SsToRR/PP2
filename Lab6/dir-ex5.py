def write_list_to_file(list_items, file_path):
    with open(file_path, mode='w') as file:
        for item in list_items:
            file.write(f"{item}\n")


write_list_to_file([1, 2, 3, 4, 5], './list_elements.txt')