try:
    text_file = open('example.txt', 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")

