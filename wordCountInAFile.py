def file_handling(file_name):
    with open(file_name, "r") as file: 
        content = file.read()
        words = content.split()
        word_count = len(words)
        return word_count

file_name = input("Enter the file path: ")

try:
    count = file_handling(file_name)
    print("Total number of words:", count)
except FileNotFoundError:
    print("File not found!")
