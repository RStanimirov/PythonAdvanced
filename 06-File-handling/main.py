# from os import listdir, path
#
#
# def traverse_dir(current_path, files_by_ext):
#     for element in listdir(current_path):
#         if path.isdir(path.join(current_path, element)):
#             traverse_dir(path.join(current_path, element), files_by_ext)
#         else:
#             extension = element.split('.')[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(element)
#
#
# files_by_ext = {}
# traverse_dir('.', files_by_ext)
#
# for ext, files in sorted(files_by_ext.items()):
#     print(f'.{ext}')
#     for x in sorted(files):
#         print(f'- - - {x}')

# Solution with walk -->
# from os import walk
#
# files_by_extension = {}
# for root, dirs, files in walk('.'):
#     for x in files:
#         extension = x.split('.')[-1]
#         if extension not in files_by_extension:
#             files_by_extension[extension] = []
#         files_by_extension[extension].append(x)
#
# with open('result.txt', 'w') as output:
#     for ext, files in sorted(files_by_extension.items()):
#         output.write(f".{ext}\n")
#         for x in sorted(files):
#             output.write(f"- - - {x}\n")


from os import walk, path

files_by_extension = {}

for _, _, files in walk('.'):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)

desktop = path.join(path.join(path.expanduser('~')), 'Desktop')

with open(path.join(path.expanduser('~'), 'Desktop', "report.txt"), "w") as output:
    for extension, files in sorted(files_by_extension.items()):
        output.write(f".{extension}\n")
        for file in sorted(files):
            output.write(f"--- {file}\n")
