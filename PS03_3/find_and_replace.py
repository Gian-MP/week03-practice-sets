file_path1 = "C:\\Users\\Admin\\Documents\\PS03_3\\filehate.txt"
file_path2 = "C:\\Users\\Admin\\Documents\\PS03_3\\filelove.txt"
old_word = "I hate kittens"
new_word = "I love kittens"



with open(file_path1, 'r') as file:
    content = file.read()

change_word = content.replace(old_word, new_word)

with open(file_path2, 'w') as new_file:
    new_file.write(change_word)

print("The file is created succesfully!")