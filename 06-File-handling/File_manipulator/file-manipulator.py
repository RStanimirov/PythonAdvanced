from os import path, remove

while True:
    line = input()
    if line == 'End':
        break

    line_parts = line.split('-')
    command = line_parts[0]
    file_name = line_parts[1]

    if command == 'Create':
        open(file_name, 'w').close()

    elif command == 'Add':
        content = line_parts[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        if path.exists(file_name):
            old_string = line_parts[2]
            new_string = line_parts[3]
            with open(file_name, 'r') as file:
                new_content = file.read().replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(new_content + '\n')
        else:
            print("An error occurred")

    elif command == 'Delete':
        if path.exists(file_name):
            remove(file_name)
        else:
            print("An error occurred")
